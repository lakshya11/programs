fin = "534976"
print fin


def swap(arr,a ,b):
  temp = arr[a]
  arr[a]=arr[b]
  arr[b] = arr[a]
  return arr

start_index = 0
rev = fin[::-1]

for index,i in enumerate(rev) :
	if rev[index]>rev[index+1]:
		pivot = index+1
		break

fin = rev[::-1]
a = sorted(fin[pivot+1::])[0]
print a

#rev = list(rev)
#rev[start_index],rev[pivot] = rev[pivot],rev[start_index]



    
