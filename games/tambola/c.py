#decide to keep username or player object in winner model
from django.forms.models import model_to_dict

def claim(request):
  username = request.GET['username']
  position = request.GET['position']
  date = datetime.date.today()

  ticket_generated = TicketGenerated.objects.get(players__username=username,date)
  ticket_status = TicketStatus.objects.get(players__username=username,date)
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

