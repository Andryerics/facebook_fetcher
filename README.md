<a href="#">
  <div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/2023_Facebook_icon.svg/1024px-2023_Facebook_icon.svg.png" width='154'/>
  </div>
</a>

<div align = "center">
<h1>Facebook FETCHER - SCRAPER</h1>
<h1>Page / Profile, Post, All Recent Post, Group (and Video), Event</h1>
<p align="center">
	<a href="#"><img src="https://img.shields.io/pypi/dm/pytube?style=flat-square" alt="pypi"/></a>
	<a href="#"><img src="https://readthedocs.org/projects/python-pytube/badge/?version=latest&style=flat-square" /></a>
	<a href="#"><img src="https://img.shields.io/badge/any%20text-you%20like-blue" /></a>
  </p>
<p>Maximize your business's potential and gain a competitive edge with our <b>four separate</b> Facebook Scrapers for: <br><b>Profile, Page, Post, All Recent Post and Group (and Video)</b>

Scrape valuable user data for lead generation, research studies, targeted marketing, sentiment analysis, data-driven decision-making, and more. 
</p>
</div>

<hr>

<h3 align="center">🔥 Unlimited Facebook Scraper & Facebook Fetcher for free -> <a href="#price-">Clack 🤝</a></h3>

<hr>


# facebook_fetcher

**facebook_fetcher** is a simple library used for scraping Facebook web pages.

# Library Information
*Author:* [**Åndry RL**](https://facebook.com/Andryerics)\
*Library:* [**facebook_fetcher**](https://github.com/MR-X-Junior/fbthon)\
*License:* [**MIT License**](https://github.com/Andryerics/facebook_fetcher/LICENSE)\
*Release:* **09**/08/20**24**\
*Version:* **0.0.2**

Since this library is still in its early version, it is likely to have many errors/bugs. If you encounter any errors/bugs in this library, feel free to post them on my [GitHub Issues](https://github.com/Andryerics/facebook_fetcher/issues) page :)

## Example of How to Use

```console
$ python -m pip install facebook_fetcher
```

### First, create a `Facebook` object

```python
>>> from facebook_fetcher import Facebook
>>> cookie = Facebook_account_cookie
>>> fb = Facebook(cookie)
```

```python
>>> from facebook_fetcher import Facebook
>>> from facebook_fetcher import Web_Login
>>> email = "example@gmail.com" # Replace this email with your Facebook account email
>>> password = "RedBullNoCounter321" # Replace this password with your Facebook account password
>>> login = Web_Login(email, password)
>>> cookie = login.get_cookie_str() # This is your Facebook account cookie
>>> fb = Facebook(cookie)
```

The method [above](#If-you-dont-have-a-Facebook-account-cookie-you-can-try-the-method-below) will log in to your Facebook account. This method may cause your Facebook account to encounter a checkpoint.

To reduce the risk of your account encountering a checkpoint, you just need to use the same user-agent as the device you last used to log in to your Facebook account.

```python
>>> from facebook_fetcher import Facebook
>>> from facebook_fetcher import Web_Login
>>> user_agent = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SM-J510GN Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'}
>>> email = "example@gmail.com" # Replace this email with your Facebook account email
>>> password = "RedBullNoCounter321" # Replace this password with your Facebook account password
>>> login = Web_Login(email, password, headers=user_agent)
>>> cookie = login.get_cookie_str() # This is your Facebook account cookie
>>> fb = Facebook(cookie)
```

#### Optional Parameters
*(For the `Web_Login` class)*.

- **email**: Facebook account email; you can also use an ID or username instead of an email
- **password**: Facebook account password
- **save_login**: Saves login information; the default value for this argument is `True`
- **free_facebook**: Use `True` if you want to use the [free.facebook.com](https://free.facebook.com) website; the default value for this argument is `False`
- **headers**: This is what will be used for the `requests` headers

### Extract Profile

The `get_profile` method can extract information from a Facebook account. This method will return a `User` object.


```python
>>> zuck = fb.get_profile('zuck')
>>> zuck.name
'Mark Zuckerberg'
>>> zuck.id
4
>>> zuck._user_info
{'name': 'Mark Zuckerberg', 'first_name': 'Mark', 'middle_name': '', 'last_name': 'Zuckerberg', 'alternate_name': '', 'about': "I'm trying to make the world a more open place.", 'username': '/zuck', 'id': '4', 'contact_info': {'Facebook': '/zuck'}, 'profile_pict': 'https://z-m-scontent.fsri1-1.fna.fbcdn.net/v/t39.30808-1/312257846_10114737758665291_6588360857015169674_n.jpg?stp=cp0_dst-jpg_e15_q65_s480x480&_nc_cat=1&ccb=1-7&_nc_sid=dbb9e7&efg=eyJpIjoiYiJ9&_nc_eui2=AeFzbmHFWdaxFtpefl6HFZsab3tzEriMmA5ve3MSuIyYDvNS3CLUOOX_Yzt_U3wSA0jeUIi3OK41Qr4CDF_Yeuxd&_nc_ohc=_tOCG5VpSrsAX8FPoj-&_nc_ad=z-m&_nc_cid=1225&_nc_eh=4613fe15e78ad080e57d79ac328ba3a7&_nc_rml=0&_nc_ht=z-m-scontent.fsri1-1.fna&oh=00_AfDS8wxbStTclGwnoPxoTGde0VDzjBQPguHMx3zTJulmkw&oe=6412E91E', 'basic_info': {'Tanggal Lahir': '14 Mei 1984', 'Jenis Kelamin': 'Laki-laki', 'Bahasa': 'English language dan Mandarin Chinese'}, 'education': [{'name': 'Harvard University', 'type': 'Computer Science and Psychology', 'study': '', 'time': '30 Agustus 2002 - 30 April 2004'}, {'name': 'Phillips Exeter Academy', 'type': 'Classics', 'study': '', 'time': 'Angkatan 2002'}, {'name': 'Ardsley High School', 'type': 'SMA', 'study': '', 'time': 'September 1998 - Juni 2000'}], 'work': [{'name': 'Chan Zuckerberg Initiative', 'time': '1 Desember 2015 - Sekarang'}, {'name': 'Meta', 'time': '4 Februari 2004 - Sekarang'}], 'living': [{'Kota Saat Ini': 'Palo Alto, California', 'Kota asal': 'Dobbs Ferry, New York'}], 'relationship': 'Berkeluarga dengan  Priscilla Chan  sejak 19 Mei 2012', 'other_name': [], 'family': [], 'year_overviews': [{'year': '2017', 'overviews': ['August Was Born', 'Harvard Degree']}, {'year': '2015', 'overviews': ['Memulai Pekerjaan Baru di Chan Zuckerberg Initiative', 'Max Lahir']}, {'year': '2012', 'overviews': ['Menikah dengan Priscilla Chan', 'Peristiwa Hidup Lain']}, {'year': '2011', 'overviews': ['Menjadi Vegetarian']}, {'year': '2010', 'overviews': ['Mulai Belajar Mandarin Chinese']}, {'year': '2009', 'overviews': ['Wore a Tie for a Whole Year']}, {'year': '2006', 'overviews': ['Launched News Feed']}, {'year': '2004', 'overviews': ['Launched the Wall', 'Memulai Pekerjaan Baru di Meta', 'Keluar dari Harvard University']}, {'year': '2002', 'overviews': ['Mulai Kuliah di Harvard University', 'Lulus dari Phillips Exeter Academy']}, {'year': '2000', 'overviews': ['Mulai Kuliah di Phillips Exeter Academy', 'Keluar dari Ardsley High School']}, {'year': '1998', 'overviews': ['Mulai Kuliah di Ardsley High School']}], 'quote': '"Fortune favors the bold."\n - Virgil, Aeneid X.284\n \n "All children are artists. The problem is how to remain an artist once you grow up." \n - Pablo Picasso\n \n "Make things as simple as possible but no simpler."\n - Albert Einstein'}
```

**Use `me` if you want to extract information from your own account**\
**Example**:


```python
>>> my_profile = fb.get_profile('me')
>>> my_profile.name
Rahmat
>>> my_profile.id
100053033144051
>>> my_profile.username
/Anjay.pro098
>>> my_profile._user_info
{'name': 'Rahmat', 'first_name': 'Rahmat', 'middle_name': '', 'last_name': '', 'alternate_name': 'Mat', 'about': '', 'username': '/Anjay.pro098', 'id': '100053033144051', 'contact_info': {'Ponsel': '0857-5462-9509', 'Facebook': '/Anjay.pro098', 'GitHub': 'MR-X-Junior', 'LinkedIn': 'rahmat-adha', 'Email': 'rahmadadha11@gmail.com'}, 'profile_pict': 'https://z-m-scontent.fsri1-1.fna.fbcdn.net/v/t39.30808-1/279908382_524601785984255_7727931677642432211_n.jpg?stp=cp0_dst-jpg_e15_p480x480_q65&_nc_cat=109&ccb=1-7&_nc_sid=dbb9e7&efg=eyJpIjoiYiJ9&_nc_eui2=AeEUCqxtmlmkSmx4EruhJj1ZoWFvcSuRApChYW9xK5ECkKEzjdDols3I7WDmPnas34nC8SsOQFYFy3zM38AIJfS1&_nc_ohc=XqfoPIkQwfkAX9oxiI4&tn=CoPUyHV9TcgsBjnY&_nc_ad=z-m&_nc_cid=1225&_nc_eh=4613fe15e78ad080e57d79ac328ba3a7&_nc_rml=0&_nc_ht=z-m-scontent.fsri1-1.fna&oh=00_AfByqAVLNVMSOfwr6pe43Iwr3HpWeVg0qImeiROkpw53rw&oe=63FCE8CF', 'basic_info': {'Tanggal Lahir': '13 Januari 2006', 'Jenis Kelamin': 'Laki-laki'}, 'education': [{'name': '', 'type': '', 'study': '', 'time': ''}], 'work': [], 'living': [{'Kota Saat Ini': 'Muaraancalung, Kalimantan Timur, Indonesia', 'Kota asal': 'Muaraancalung, Kalimantan Timur, Indonesia'}], 'relationship': 'Lajang', 'other_name': {'Nama panggilan': 'Met'}, 'family': [{'name': 'Pahrul Aguspriana XD.', 'username': '/PahrulXD', 'designation': 'Adik laki-laki', 'profile_pict': 'https://z-m-scontent.fsri1-1.fna.fbcdn.net/v/t39.30808-1/331028920_3040847712882567_3539568768564278719_n.jpg?stp=c0.0.320.320a_cp0_dst-jpg_e15_p320x320_q65&_nc_cat=101&ccb=1-7&_nc_sid=dbb9e7&efg=eyJpIjoiYiJ9&_nc_eui2=AeEW2pBM_jo0ZzypEALp1QB7eG7Nm80Gj5J4bs2bzQaPkmGYk_gZVtPSzsrb1SX796_BwslIoWRa_4yIuFC3x1Fh&_nc_ohc=NjtS1hHD7GcAX9Sp4HY&_nc_ad=z-m&_nc_cid=1225&_nc_eh=4613fe15e78ad080e57d79ac328ba3a7&_nc_rml=0&_nc_ht=z-m-scontent.fsri1-1.fna&oh=00_AfBGUpSnDzv3tHfsng6gWLn2ZGjNwSaFXzDLeCnlWv9Lsg&oe=63FDEBC2'}], 'year_overviews': [], 'quote': "i know i'm not alone"}
```

### Update Profile Picture
You can use the `UpdateProfilePicture` function to change your Facebook account's profile picture.

**Example:**

```python
from facebook_fetcher import settings
from facebook_fetcher import Facebook

fb = Facebook("datr=klr23aug21xxxxxxx") # Facebook Account Cookie 

settings.UpdateProfilePicture(fb, photo='/sdcard/DCIM/Orang-Susah.jpg')
```

#### Result

##### Before 

![Before Update Profile Picture](https://i.ibb.co/tzpq34P/IMG-20230419-202908.jpg)

##### After

![After Update Profile Picture](https://i.ibb.co/wJCp0HD/IMG-20230419-203029.jpg)

### Get Notifications
You can use the `get_notifications` method to retrieve the latest notifications from your Facebook account.

**Example:**


```python
no = fb.get_notifications(limit = 2)

for chaa in no:
  print ("Message : "+ chaa['message'])
  print ("Time : "+ chaa['time'])
  print ("Redirect URL : "+ chaa['redirect_url'] + "\n")
```

**Output:**

```
Message: Based on pages that interact with you, you might like Meme Upin Ipin Comic Lucu.                               
Time: April 11                                                         
Redirect URL: https://mbasic.facebook.com/a/notifications.php?redir=%2Fgroups%2F426298749190770%2F&seennotification=1681152051803754&eav=AfbWn5_N4XPZ0dL2bdBlHmCJIqmlGanPyx8_K3EuoQ47EREpeYdQtHn-1DmRfQaTNE0&gfid=AQDZ4pcYOl5JlPJd0uw&paipv=0&refid=48                                 

Message: Based on pages that interact with you, you might like Mukbang Yummy Food.
                                
Time : 8 Apr
Redirect URL : https://mbasic.facebook.com/a/notifications.php?redir=%2Fgroups%2F340989278132975%2F&seennotification=1680900355646527&eav=AfZlnRarakilRKNOhz6fPULFLUjDyccZvOhpJFhWEAy2un9H6EbgdPZ7Zii39UuMazc&gfid=AQBuf1_B6NbYKhXjCv8&paipv=0&refid=48
```

### Get Posts

The `get_posts` method will collect and extract posts, and this method will return a `list` containing a collection of `Posts` objects.

**NOTE: THIS METHOD CAN ONLY COLLECT POSTS FROM USER ACCOUNTS, IT CANNOT COLLECT POSTS FROM GROUPS OR PAGES.**

```python
for x in fb.get_posts('zuck', limit = 2):
   print("Author : "+x.author)
   print("Caption: "+x.caption)
   print("Upload Time "+ x.upload_time + "\n\n")
```

#### Output
```python
Author : Mark Zuckerberg
Caption: When Priscilla and I started working on the Chan Zuckerberg Initiative's science mission to help cure, prevent or manage all diseases, our first major project was launching the Biohub. It has been very successful, so today we're launching a second Biohub in Chicago that will engineer miniaturized sensors to instrument living tissues to help scientists see and understand how cells work together. We're going to start by instrumenting skin and heart tissues with an initial focus on measuring inflammation. About 50% of deaths are caused by diseases related to inflammation, like cancer and heart disease, so we're hopeful the technology created at the Chicago Biohub will have broad applications for science and health similar to the San Francisco Biohub.
Upload Time 2 Maret pukul 16.00


Author : Mark Zuckerberg
Caption: We're creating a new top-level product group at Meta focused on generative AI to turbocharge our work in this area. We're starting by pulling together a lot of the teams working on generative AI across the company into one group focused on building delightful experiences around this technology into all of our different products. In the short term, we'll focus on building creative and expressive tools. Over the longer term, we'll focus on developing AI personas that can help people in a variety of ways. We're exploring experiences with text (like chat in WhatsApp and Messenger), with images (like creative Instagram filters and ad formats), and with video and multi-modal experiences. We have a lot of foundational work to do before getting to the really futuristic experiences, but I'm excited about all of the new things we'll build along the way.
Upload Time 27 Februari pukul 20.50
```

### Post Parser

The `post_parser` method is used to extract posts, and this method will return a `Posts` object.


```python
>>> post = fb.post_parser("https://m.facebook.com/story.php?story_fbid=pfbid02kbL4vnSF4Ex88nBQrMZdvjUoWV7hhznHZ8BpMcFAJzjL2CEoBCAHeHEk4Y8DLAQ5l&id=100053033144051&mibextid=Nif5oz")
>>> post.author
Rahmat
>>> post.caption
Hello World 🌍
>>> post.post_file
{'image': [{'link': 'https://z-m-scontent.fsri1-1.fna.fbcdn.net/v/t39.30808-6/241434705_371774571266978_6844800659294160676_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=104&ccb=1-7&_nc_sid=110474&efg=eyJpIjoiYiJ9&_nc_eui2=AeE-bGgqsChJWa0bm9hnBZ-c9HuYP8xaWmP0e5g_zFpaYypDCKSWUSxTvpaIdTGIXCGEzD4653spgkhYVI1L37UK&_nc_ohc=3B_9FgPbsqgAX_k1QAl&_nc_ad=z-m&_nc_cid=1225&_nc_eh=4613fe15e78ad080e57d79ac328ba3a7&_nc_zt=23&_nc_rml=0&_nc_ht=z-m-scontent.fsri1-1.fna&oh=00_AfB8x_I9eObguAKc3CVt2A1dYWAYrLDpzMOnD3CnvfM4wg&oe=641513CF', 'id': '241434705_371774571266978_6844800659294160676', 'preview': 'https://z-m-scontent.fsri1-1.fna.fbcdn.net/v/t39.30808-6/241434705_371774571266978_6844800659294160676_n.jpg?stp=cp0_dst-jpg_e15_p526x296_q65&_nc_cat=104&ccb=1-7&_nc_sid=110474&efg=eyJpIjoiYiJ9&_nc_eui2=AeE-bGgqsChJWa0bm9hnBZ-c9HuYP8xaWmP0e5g_zFpaYypDCKSWUSxTvpaIdTGIXCGEzD4653spgkhYVI1L37UK&_nc_ohc=3B_9FgPbsqgAX_k1QAl&_nc_ad=z-m&_nc_cid=1225&_nc_eh=4613fe15e78ad080e57d79ac328ba3a7&_nc_zt=23&_nc_rml=0&_nc_ht=z-m-scontent.fsri1-1.fna&oh=00_AfD3FkrA5grtqsZFr7LoQKSVpQToVBhEXRqC3ntmUjB5Hw&oe=641513CF', 'content-type': 'image/jpeg'}], 'video': []}
>>> post.upload_time
17 Mei 2021 pukul 13.15
>>> post.post_datetime
datetime.datetime(2021, 5, 17, 21, 15, 17)
>>> post.get_react()
{'like': 5652, 'love': 310, 'care': 9, 'haha': 6, 'wow': 252, 'sad': 0, 'angry': 1}
```

#### Sending Comments

You can use the `send_comment` method to post a comment.
The `send_comment` method will return `True` if the comment is successfully sent.

**Example:**


```python
>>> post = fb.post_parser('https://m.facebook.com/story.php?story_fbid=pfbid0h1BPgqZsa4seKWoqn7c6GqDyAD3vKUePuasDRHuZCyN46M4uuAVy4m4fAukRvaojl&id=100053033144051&mibextid=Nif5oz')
>>> post.send_comment('Hallo kak '+post.author +'\n\nKomentar ini di tulis menggunakan library fbthon :)')
True
```

##### Result
**See the comment at the bottom**

![Example of how to send a comment](https://i.ibb.co/QFDpnw9/Screenshot-20230322-064024.jpg)

To add a photo to the comment, you can use the `file` argument.

**Example:**


```python
>>> post = fb.post_parser('https://m.facebook.com/story.php?story_fbid=pfbid02kTobxSiD9buMUEjrq57FFnhQ6FJyGnafmNhMimoaamoAwuECAjboYaB6mE7C7pPZl&id=100053033144051&mibextid=Nif5oz')
>>> post.send_comment("Komentar ini tidak di sertai dengan foto!")
True
>>> post.send_comment("Komentar ini di sertai dengan foto!", file = "/sdcard/DCIM/Facebook/FB_IMG_1681559707400.jpg")
True
```

##### Result

![Example of sending a comment with a photo](https://i.ibb.co/6vd6BQc/IMG-20230418-110223.jpg)

#### Reacting to Posts

You can use the `send_react` method to react to a post.
This method will return `True` if the reaction is successfully applied to the post.


```python
>>> post = fb.post_parser(Link_post_facebook)
>>> post.send_react(react_type)
True
```

There are 7 reaction types, including:
- Like
- Love
- Care
- Haha
- Wow
- Sad
- Angry

**Example of how to send a reaction:**

```python
>>> post = fb.post_parser('https://m.facebook.com/story.php?story_fbid=pfbid0h1BPgqZsa4seKWoqn7c6GqDyAD3vKUePuasDRHuZCyN46M4uuAVy4m4fAukRvaojl&id=100053033144051&mibextid=Nif5oz')
>>> post.send_react('Wow')
True
```

##### Result
![Example of reacting to a post](https://i.ibb.co/SPXGWJJ/Screenshot-2023-0322-065521.png)

##### Sharing a Post
You can use the `share_post` method to share someone else's post to your Facebook account.

**Example (1):**


```python
post = fb.post_parser("https://m.facebook.com/story.php?story_fbid=pfbid0gxnxN5dZDDA93S2GveyxqgSzEdYdAtdE32PYyAd7iftDS7yBHprBACc9VcFXDoPtl&id=100053033144051&mibextid=Nif5oz")
post.share_post()
```

##### Result

![Example of sharing a post](https://i.ibb.co/F39c30w/IMG-20230419-064244.jpg)

**Example (2):**

You can also add `message`, `location`, and `feeling` to the shared post.


```python
post = fb.post_parser("https://m.facebook.com/story.php?story_fbid=pfbid0gxnxN5dZDDA93S2GveyxqgSzEdYdAtdE32PYyAd7iftDS7yBHprBACc9VcFXDoPtl&id=100053033144051&mibextid=Nif5oz")
post.share_post(message = "Postingan ini di bagikan menggunakan library fbthon", location = "Kuningan Timur", feeling = "Happy")
```

##### Result
![Example of sharing a post with message, location, and feeling](https://i.ibb.co/7J1wzB2/IMG-20230419-070541.jpg)

### Messenger

The `Messenger` object can be used to send/receive chats.\
There are 2 ways to create a `Messenger` object:

**Method 1**

```python
>>> msg = fb.Messenger()
```
**Method 2**

```python
>>> from facebook_fetcher import Messenger
>>> msg = Messenger(Your_Facebook_Account_Cookie)
```


#### Getting New Messages
The `get_new_message` method can be used to retrieve new messages :)

```python
for x in msg.get_new_message(limit=3):
   print("Name: " + x['name'])
   print("Account ID: " + x['id'])
   print("Last Chat: " + x['last_chat'])
   print("Time: " + x['time'] + "\n\n")


```

##### Output

```python
Name: Khaneysia                        
Account ID: 1000xxxxxxxxxxx
Last Chat: Good Night sayang :)
Time: 5 minutes ago

Name: Rahmat
Account ID: 100053033144051
Last Chat: Hallo Kak Rahmat :)
Time: 11 minutes ago

Name: Mark Zuckerberg
Account ID: 4
Last Chat: Ban my account, please                          
Time: March 4

```

The `get_new_chat` method can also be used to retrieve new messages, but this method is different from the `get_new_message` method.

```python
>>> msg.get_new_message(limit = 3)
[{'name': 'Khaneysia', 'id': '1000xxxxxxxxxxx', 'last_chat': 'Good Night sayang :)', 'time': '23 menit lalu'}, {'name': 'Rahmat', 'id': '100053033144051', 'last_chat': 'Hallo Kak Rahmat:)', 'time': '34 menit lalu'}, {'name': 'Mark Zuckerberg', 'id': '4', 'last_chat': 'Hello Mark Zuckerberg', 'time': '4 Mar'}]
>>> msg.get_new_chat(limit = 3)
[Facebook Chats : name='Mark Zuckerberg' id=4 chat_id=4:100090156622219 type='user', Facebook Chats : name='Khaneysia' id=1000xxxxxxxxxxx chat_id=1000xxxxxxxxxxx:100090156622219 type='user', Facebook Chats : name='Rahmat' id=100053033144051 chat_id=100053033144051:100090156622219 type='user']
```

From the code above, we can conclude the difference between the `get_new_message` and `get_new_chat` methods.

The `get_new_message` method returns a `list` containing a collection of `dict` objects, whereas the `get_new_chat` method returns a `list` containing a collection of `Chats` objects.

#### Sending Messages

You can use the `new_chat` method to send messages. This method will return a `Chats` object.


```python
with msg.new_chat('zuck') as chat:
  chat.send_text('Assalamualaikum')
  chat.send_text('Hallo om '+ chat.name)
  chat.send_text('Apa kabar?')
  chat.send_text('Pesan ini di kirim menggunakan library fbthon:)\n\nTerima kasih Sudah membaca chat saya.')
```

##### Result
![Example of Sending a Message](https://i.ibb.co/fQHtDmb/Screenshot-20230317-222932.jpg)

You can use the `send_image` method to send a chat with a photo.

**Example:**


```python
with msg.new_chat("Anjay.pro098") as chat:
  chat.send_text("Hallo kak "+chat.name)
  chat.send_text("Pesan ini di kirim menggunakan library fbthon :)")
  chat.send_image(file = "/sdcard/DCIM/Facebook/FB_IMG_1681559707400.jpg",message = "Aku ketika nunggu buka puasa : ")
  chat.send_like_stiker()
```

##### Result
![Example of sending a chat with a photo](https://i.ibb.co/FVgZ7Mf/IMG-20230418-184806.jpg)

## Creating Posts
The `create_timeline` method can be used to create posts. This method will return `True` if the post is successfully created.

### Creating a Post (Caption Only)

```python
>>> fb.create_timeline(target='me', message='This post was created using the fbthon library\n\nHehe :>')
True
```

#### Result
![Creating a Post (Caption Only)](https://i.ibb.co/wB998Yd/Screenshot-2023-0317-224853.png)

### Creating a Post on a Friend's Account
To create a post on a friend's account, you just need to change the `target` parameter to the ID or username of your friend :)

**Example:**

```python
>>> fb.create_timeline(target='Friend’s ID or username', message='This post was created using the fbthon library\n\nHehe :>')
True
```

#### Result
![Creating a Post (Caption Only) on a Friend’s Facebook Account](https://i.ibb.co/cTwRYDh/IMG-20230318-181857.jpg)

### Creating a Post (Tagging Friends)
To tag friends in a post, you can use the `users_with` argument.

```python
>>> fb.create_timeline(target='me', message='This post was created using the fbthon library\n\nHehe :>', users_with='friend’s Facebook ID')
True
```

#### Result
![Creating a Post (Tagging Friends)](https://i.ibb.co/tbHKb0x/IMG-20230322-072612.jpg)

### Creating a Post (With Photo)
You can use the `file` argument to add a photo to your post :)

```python
>>> fb.create_timeline(target='me', message='Alhamdulillah :)', file='/sdcard/Pictures/Certificate/mimo-certificates-125_page-0001.jpg')
True
```

#### Result
![Creating a Post (With Photo)](https://i.ibb.co/d4nKvVr/Screenshot-2023-0318-151426.png)

Also, you can use the `filter_type` argument to apply a filter to the photo you are uploading.

```python
>>> fb.create_timeline(target='me', message='Alhamdulillah :)', file='/sdcard/Pictures/Certificate/mimo-certificates-125_page-0001.jpg', filter_type='1')
True
```

And here is the result:

![Applying a Filter to a Photo](https://i.ibb.co/twf0tnc/Screenshot-2023-0323-082948.png)

**There are several filter types you can try, including:**
- No Filter = -1
- Black and White = 1
- Retro = 2

### Creating a Post (With Location)
You can use the `location` argument to add a location to your post.

```python
>>> fb.create_timeline(target='me', message='This post was created using the fbthon library\n\nHehe :>', location='Muaraancalung, Kalimantan Timur')
True
```

#### Result
![Creating a Post (With Location)](https://i.ibb.co/vh5zh05/Screenshot-2023-0318-145829.png)

### Creating a Post (With Feeling)
You can use the `feeling` argument to add a feeling to your post.

```python
>>> fb.create_timeline(target='me', message='This post was created using the fbthon library\n\nHehe :>', feeling='Happy')
True
```

#### Result
![Creating a Post (With Feeling)](https://i.ibb.co/n7yp62b/Screenshot-2023-0318-152335.png)

### Create a Facebook Account
You can use the `CreateAccount` class to create a Facebook account.

**NOTE: This feature is still experimental, so it may not work reliably.**

#### Example:

Below is a simple program to create a Facebook account.

```python
import sys
from facebook_fetcher import CreateAccount

print("[+] Create Facebook Account [+]\n")

firstname = input("[?] First Name: ") # First Name
lastname = input("[?] Last Name: ") # Last Name
email = input("[?] Email/Phone: ") # Email Address / Phone Number
gender = input("[?] Gender (Male/Female): ") # Gender
birthday = input("[?] Date of Birth (DD/MM/YYYY): ") # Date of Birth
password = input("[?] Password: ") # Password

new_account = CreateAccount(firstname=firstname, lastname=lastname, email=email, gender=gender, date_of_birth=birthday, password=password)

print("\n[+] Enter the verification code sent to " + email)
verification_code = input("[?] Verification Code: ")

# The `confirm_account` method will return `True` if the account is successfully confirmed.
confirmation = new_account.confirm_account(verification_code)

if confirmation:
    print("[✓] Successfully Created Facebook Account :)\n")
    print("[+] Account Name: %s %s" % (firstname, lastname))
    print("[+] Account ID: %s" % (new_account.get_cookie_dict()['c_user']))
    print("[+] Email/Phone: %s" % (email))
    print("[+] Gender: %s" % (gender))
    print("[+] Date of Birth: %s" % (birthday))
    print("[+] Password: %s" % (password))
    print("[+] Account Cookie: %s" % (new_account.get_cookie_str()))
    print("[+] Account Token: %s" % (new_account.get_token()))
    sys.exit(0)
else:
    print("[!] Failed to Create Facebook Account")
    sys.exit(1)
```

##### Running the Program
![Running the script to create a Facebook account using the fbthon library](https://i.ibb.co/2Sd19Wc/Screenshot-2023-0420-093249.png)

###### Result
This is the account created using the fbthon library :)

![This is a Facebook account created using the fbthon library](https://i.ibb.co/7K3q3hj/Screenshot-20230420-093826.jpg)

#### Optional Parameters
*(For the `CreateAccount` class)*

- **firstname**: First Name
- **lastname**: Last Name
- **email**: Email address to be used for registering a Facebook account. You can also use a phone number instead of an email address.
- **gender**: Gender (Male/Female)
- **date_of_birth**: Date of birth in the format DD/MM/YYYY, Example: 13/01/2006
- **password**: Password to be used for creating the Facebook account.

# Installation

**fbthon** is available on PyPi.


```console
$ python -m pip install facebook_fetcher
```

**fbthon** can be installed on Python version 3.7+.
