from datetime import datetime
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response, HttpResponseRedirect, redirect
from django.template import RequestContext
from inventory_app.forms import *
from inventory_app.models import Equipment, Part
from utils import authenticate_user


def jda_login(request):
  ctx = {"msg": ""}
  if request.user.id:
    return HttpResponseRedirect("/home/")
  login_form = LoginForm()
  if request.POST:
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
      try:
        success = authenticate_user(request, request.POST["username"], request.POST["password"])
      except Exception as e:
        success = False
      if success:
        return HttpResponseRedirect("/home/")
  ctx["login_form"] = login_form
  return render_to_response("login.html", ctx, context_instance=RequestContext(request))


def logout_user(request):
  logout(request)
  return HttpResponseRedirect("/")


def manage_admins(request):
  if not request.user.id or not request.user.is_superuser:
    return HttpResponseRedirect("/")
  users = User.objects.all()
  ctx = {"users": users}
  ctx["user_form"] = AddUserForm()
  ctx["msgs"] = get_message_list(request.user)
  return render_to_response("manage_admins.html", ctx, context_instance=RequestContext(request))


def add_user(request):
  if not request.user.id or not request.user.is_superuser:
    return HttpResponseRedirect("/")

  msgs = []
  try:
      if request.POST:
        u_form = AddUserForm(request.POST)
        if u_form.is_valid():
            if request.POST["password"] == request.POST["confirm_password"]:
                user = User(username=request.POST["username"], email=request.POST["email"])
                user.set_password(request.POST["password"])
                user.save()
            else:
                msgs.append("Password does not matched.")
        else:
          append_errors(u_form.errors, msgs)
  except Exception as e:
      msgs.append(e.message)

  set_message(request.user, msgs)
  return redirect("/manage-admins/")


def set_status(request, uid, status):
  if not request.user.id:
    return HttpResponseRedirect("/")
  u_status = False
  if status == 'True':
    u_status = True
  u = User.objects.get(id=uid)
  u.is_active = u_status
  u.save()
  return HttpResponseRedirect("/manage-admins/")


def home(request):
  if not request.user.id:
    return HttpResponseRedirect("/")
  ctx = {"user": request.user, "next_page": None, "prev_page": None}
  page = 1
  if request.GET.get("page"):
    page = int(request.GET.get("page"))
  search = request.GET.get("search")
  if search:
    equipments = Equipment.objects.filter(tag__icontains=search)
    ctx["search"] = search
  else:
    equipments = Equipment.objects.all()
  try:
    equipments = Paginator(equipments, 20).page(page)
  except:
    equipments = []
  if len(equipments) == 20:
    ctx["next_page"] = page+1
  if page>1:
    ctx["prev_page"] = page-1
  ctx["equipments"] = equipments
  ctx["msgs"] = get_message_list(request.user)
  return render_to_response("home.html", ctx, context_instance=RequestContext(request))

def equipment(request, tag):
  if not request.user.id:
    return HttpResponseRedirect("/")
  ctx = {"user": request.user, "next_page": None, "prev_page": None}
  page = 1
  if request.GET.get("page"):
    page = int(request.GET.get("page"))
  search = request.GET.get("search")
  equipment_ = Equipment.objects.get(tag=tag)
  if search:
    parts = Part.objects.filter(equipment=equipment_, code__icontains=search)
    ctx["search"] = search
  else:
    parts = Part.objects.filter(equipment=equipment_)
  try:
    parts = Paginator(parts, 20).page(page)
  except:
    parts = []
  if len(parts) == 20:
    ctx["next_page"] = page+1
  if page>1:
    ctx["prev_page"] = page-1
  ctx["parts"] = parts
  ctx["equipment"] = equipment_
  return render_to_response("equipment.html", ctx, context_instance=RequestContext(request))


def add_equipment(request):
  if not request.user.id:
    return HttpResponseRedirect("/")
  ctx = {"user": request.user}
  eq_form = EquipmentForm()
  msgs = []
  if request.POST:
    eq_form = EquipmentForm(request.POST)
    try:
      if eq_form.is_valid():
        eq = Equipment(tag=request.POST["tag"], description=request.POST["description"], location=request.POST["location"])
        eq.save()
        return HttpResponseRedirect("/")
    except:
      msgs.append("Error in saving.")

  ctx["msgs"] = msgs
  ctx["eq_form"] = eq_form
  return render_to_response("add_equipment.html", ctx, context_instance=RequestContext(request))


def add_part(request, tag):
  if not request.user.id:
    return HttpResponseRedirect("/")
  ctx = {"user": request.user}
  part_form = PartForm()
  msgs = []
  try:
    eq = Equipment.objects.get(tag=tag)
    ctx["eq"] = eq
    if request.POST:
      part_form = PartForm(request.POST)
      if part_form.is_valid():
        part = Part(code=request.POST["code"], description=request.POST["description"],
                     location=request.POST["location"], part_number=request.POST["part_number"],
                     quantity=request.POST["quantity"], max_level=request.POST["max_level"],
                     min_level=request.POST["min_level"], reorder_point=request.POST["reorder_point"],
                     last_price=request.POST["last_price"], currency_id=request.POST["currency"],
                     vendor_detail=request.POST["vendor_detail"])
        part.equipment = eq
        part.save()
        return HttpResponseRedirect("/equipment/%s/"%eq.tag)
  except Exception as e:
    msgs.append("Error in saving.")
    ctx["msgs"] = msgs
  ctx["part_form"] = part_form
  ctx["currency"] = Currency.objects.all()
  return render_to_response("add_part.html", ctx, context_instance=RequestContext(request))


def part(request, code):
  if not request.user.id:
    return HttpResponseRedirect("/")
  ctx = {"user": request.user}
  ctx["issue_form"] = IssueForm()
  ctx["msgs"] = get_message_list(request.user)
  try:
    ctx["part"] = Part.objects.get(code=code)
  except:
    ctx["msgs"].append("part not found.")
  return render_to_response("part.html", ctx, context_instance=RequestContext(request))


def edit_part(request, code):
  if not request.user.id:
    return HttpResponseRedirect("/")
  ctx = {"user": request.user}
  try:
    if request.POST:
      _part = Part.objects.get(code=code)
      part_form = PartForm(request.POST, instance=_part)
      if part_form.is_valid():
        _part.quantity = request.POST["quantity"]
        _part.max_level = request.POST["max_level"]
        _part.min_level = request.POST["min_level"]
        _part.reorder_point = request.POST["reorder_point"]
        _part.last_price = request.POST["last_price"]
        _part.currency_id = request.POST["currency"]
        _part.description = request.POST["description"]
        _part.location = request.POST["location"]
        _part.vendor_detail = request.POST["vendor_detail"]
        _part.save()
        return HttpResponseRedirect("/part/%s/"%_part.code)
    else:
      _part = Part.objects.get(code=code)
      part_form = PartForm(instance=_part)
      part_form.set_read_only(True)
      ctx["currency"] = Currency.objects.all()
      ctx["edit"] = True
  except Exception as e:
    ctx["msgs"].append("part not found.")

  ctx["part_form"] = part_form
  return render_to_response("add_part.html", ctx, context_instance=RequestContext(request))


def issue_part(request, code):
  if not request.user.id:
    return HttpResponseRedirect("/")
  msgs = []
  try:
    i_form = IssueForm(request.POST)
    if i_form.is_valid():
      _part = Part.objects.get(code=code)
      _part.issued_to = request.POST["issued_to"]
      _part.issued_by = request.user
      _part.issued_date = datetime.utcnow()
      _part.save()
      part_log = PartLog(part=_part, description=_part.description, location=_part.location, quantity=_part.quantity,
                         issued_by=_part.issued_by, issued_to=_part.issued_to, issued_date=_part.issued_date)
      part_log.save()
      return HttpResponseRedirect('/part/%s/'%code)
    else:
      append_errors(i_form.errors, msgs)
      msgs[0] = msgs[0].replace("This", "Issued To")
  except:
    msgs.append("part not found.")
  set_message(request.user, msgs)
  return HttpResponseRedirect('/part/%s/'%code)


def issue_history(request, code):
  if not request.user.id:
    return HttpResponseRedirect("/")
  ctx = {"user": request.user, "next_page": None, "prev_page": None}
  page = 1
  if request.GET.get("page"):
    page = int(request.GET.get("page"))
  part_log = PartLog.objects.filter(part__code=code)
  try:
    part_log = Paginator(part_log, 20).page(page)
  except:
    part_log = []
  if len(part_log) == 20:
    ctx["next_page"] = page+1
  if page>1:
    ctx["prev_page"] = page-1
  ctx["part_log"] = part_log
  if part_log:
    ctx["part"] = part_log[0].part
  return render_to_response("part_history.html", ctx, context_instance=RequestContext(request))


def get_message_list(user):
  msgs = [msg.message for msg in user.message_set.all()]
  user.message_set.all().delete()
  return msgs


def set_message(user, msg_list):
  for msg in msg_list:
    user.message_set.create(message=msg)


def append_errors(error_dict, msgs):
  for key, value in error_dict.iteritems():
      msgs.append(value[0])
