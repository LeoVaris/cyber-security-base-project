from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import user_query, User, Comments

def index(req):
  return render(req, 'index.html')

@csrf_exempt
def sql(req):
  res = []
  if req.method == 'GET':
    return render(req, 'form_sql_injection.html', { "results": res, "empty": True })

  name = req.POST.get('first name')
  if name == '':
    return redirect('/SQL_injection')
  res = user_query(name.capitalize())
  return render(req, 'form_sql_injection.html', { "results": res, "empty": False })

@csrf_exempt
def broken_auth(req):
  if req.method == 'GET':
    return render(req, 'login.html')
  
  username = req.POST.get('username')
  password = req.POST.get('password')

  user = User.objects.filter(username=username, password=password).first()
  if user:
    req.session.clear()
    req.session['username'] = username
    req.session.permanent = True
    if req.session['username'] == 'admin':
      return redirect('/')
    else:
      return redirect('/user_lounge')
  
  return redirect('/broken_auth')

def lounge(req):
  username = req.session['username']
  if not username is None:
    return render(req, 'user_lounge.html', { "username": username} )
  return redirect('/broken_auth')

def logout(req):
  req.session.clear()
  return redirect('/broken_auth')

@csrf_exempt
def xss(req):
  if req.method == 'GET':
    comments = [] # get from db
    return render(req, 'xss.html', { "posts":comments })

  comment = req.POST.get('comment')
  if comment == '':
    return render(req, 'xss.html', {"posts": []})
  new_c = Comments(comment=comment)
  new_c.save()

  # add to db
  comments = Comments.objects.all()
  return render(req, 'xss.html', {"posts": comments})
"""

{% with messages = get_flashed_messages() %}
          {% if messages %}
              <div class="alert-info">
              {% for message in messages %}
                  <p>{{ message }}</p>
              {% endfor %}
              </div>
          {% endif %}
      {% endwith %}

"""