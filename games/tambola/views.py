#decide to keep username or player object in winner model
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from .models import Players
from .models import TokensGenerated
from .models import TicketsGenerated
from .models import TicketsStatus
import random
from datetime import datetime

def index(request):
  data = {'a':1}
  #username = request.GET['username'] uncomment later
  username = 'lbansal'
  date = datetime.now().date()
  ticket_generated = TicketsGenerated.objects.get(player__username=username,date=date)
  ticket_status = TicketsStatus.objects.get(player__username=username,date=date)
  data['ticket_status'] = ticket_status
  data['ticket_generated'] = ticket_generated
  print "ticket generated",ticket_generated
  print "ticket_status" ,ticket_status
  return render(request, 'index.html', data)

def ticket_generation(request):
  users = Players.objects.order_by('username')
  for user in users:
    numbers = range(1,100)
    random.shuffle(numbers)
    raw_ticket = [["","","",""],["","","",""],["","","",""]]
    for i in xrange(len(raw_tickets)):
      for j in xrange(0,5):
        raw_ticket[i].append(numbers[i*5+j])
      random.shuffle(raw_ticket[i])

    #ticket coordinates  
    x1 = raw_ticket[0][0]
    x2 = raw_ticket[0][1]
    x3 = raw_ticket[0][2] 
    x4 = raw_ticket[0][3] 
    x5 = raw_ticket[0][4] 
    x6 = raw_ticket[0][5] 
    x7 = raw_ticket[0][6] 
    x8 = raw_ticket[0][7] 
    x9 = raw_ticket[0][8] 
    y1 = raw_ticket[1][0]
    y2 = raw_ticket[1][1]
    y3 = raw_ticket[1][2] 
    y4 = raw_ticket[1][3] 
    y5 = raw_ticket[1][4] 
    y6 = raw_ticket[1][5] 
    y7 = raw_ticket[1][6] 
    y8 = raw_ticket[1][7] 
    y9 = raw_ticket[1][8]
    z1 = raw_ticket[2][0]
    z2 = raw_ticket[2][1]
    z3 = raw_ticket[2][2] 
    z4 = raw_ticket[2][3] 
    z5 = raw_ticket[2][4] 
    z6 = raw_ticket[2][5] 
    z7 = raw_ticket[2][6] 
    z8 = raw_ticket[2][7] 
    z9 = raw_ticket[2][8] 
    
    #insert into tambola_t = ticket_generated
    #insert into tambola_c = ticket_status
  return render(request, 'GenerateTicket.html', 'Tickets added successfuly')

def ticket_display(request):
  pass



def claim(request):
  username = request.GET['username']
  position = request.GET['position']
  date = datetime.date.today()

  ticket_generated = TicketGenerated.objects.get(players__username=username,date=date)
  ticket_status = TicketStatus.objects.get(players__username=username,date=date)
  ticket_g = ticket_generated['ticket']
  ticket_s = ticket_status['ticket']

  top_left_match = top_right_match = bottom_left_match = bottom_right_match = False
  # convert model to dictionary
  #tocket_g = model_to_dict(ticket_g, fields=[], exclude=[])

  #iterating over the fields of model
  #TODO://to test
  for index in xrange(1,10):
    coord_xl = 'x'+str(index)
    if ticket_g[coord_xl] and ticket_g[coord_xl] == ticket_s[coord_xl] :
      top_left_match = True
    
    coord_zl = 'z'+str(index)
    if ticket_g[coord_zl] and ticket_g[coord_zl] == ticket_s[coord_zl]:
      bottom_left_match = True
    
    coord_xr = 'x'+ str(10-index)
    if ticket_g[coord_xr]  and ticket_g[coord_xr] == ticket_s[coord_xr]:
      top_right_match = True

    coord_zr = 'z'+str(10-index)
    if ticket_g[coord_zr] and ticket_s[coord_zr] == ticket_s[coord_zr]:
      bottom_right_match = True


  if top_left_match and top_right_match and bottom_left_match and bottom_right_match:
    corner_winner = Winners.objects.get(date=date,position='corners')
    if corner_winner['username']!= username:
      messegae= "Already claimed"
    else :
      winner = Winner(username=username,date=date,position='Corner')
      winner.save()



def check(request):
  date = datetime.date.today()
  username = request.GET['username']

  player_ticket = TicketsGenerated.objetcs.get(player__username=username,date=date)

  tokens_generated = TokensGenerated.objects.order_by('time')
  for token in tokens_generated:
    if (token['time'] <= datetime.now("Y-m-d H:i:s")) and (token['number']== request.GET['val']):

      checked_token_pos = 0
      
      for i in xrange(1,10):
        x_coordinate = 'x'+str(i)
        if request.GET['val'] == player_ticket[x_coordinate]:
          checked_token_pos = x_coordinate
          break
        y_coordinate = 'y'+str(i)
        if request.GET['val'] == player_ticket[y_coordinate]:
          checked_token_pos = y_coordinate
          break
        z_coordinate = 'z'+str(i)
        if request.GET['val'] == player_ticket[z_coordinate]:
          checked_token_pos = z_coordinate
          break 

  if checked_token_pos:
    #update query
    '''
    mysqli_query($con,"UPDATE tambola_c SET ".$val1."=".$_GET['val']." where ldab = '".$_GET['ldab']."' AND date = '".date("Y-m-d")."'");
          echo $val1 . "<br>" . $_GET['ldab'];
    '''





def last_number_annouced(request):
  pass


def numbers_announced(request):
  '''
  select from token_gen order by time
  '''


def number_generation(request,):
  '''
  Take duration as input:at which token will randomly generated 
  view for generating and inserting random number
   from 1-100 into "token_gen" table
  and at which time which number will be announced
  Ref :2.php
  '''
  winners = Winner.objects.all()
  winners.delete()

  tokens_generated = TokensGenerated.objects.all()
  tokens_generated.delete()

  date = datetime.today() 

  tokens = range(1,100)
  randome.shuffle(tokens)

  for token in tokens:
    # date = date + duration add duration into date
    t = TokensGenerated(token=token,date=date) # check







