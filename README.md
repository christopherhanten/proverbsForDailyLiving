#<b>Proverbs For Daily Living</b><br/><br/>
Trello: https://trello.com/b/bAKfRrG9/proverbfordailyliving<br/><br/>

<b>Color Palette</b><br/>

|hex code|color|
|---|---|
|#baa085|Light brown(the color of the old book pages)|
|#a31917|maroon(the color of the illustrations)|
|#2ff6f2|Teal(for accents)|
|#000000|Black|
|#FFFFFF|White|
<br/>


<b>Pages</b><br/>
<ul>
<li><b>About:</b> what the app is for and what I hope for</li><br/>
  <li><b>Index:</b> See the daily proverb. Add a proverb with textarea and submit button</li><br/>
  <li><b>Prayer List</b>: a place to add people to the prayer list and also sign up to be a prayerperson</li><br/>
  <li><b>Tenets:</b> a read-only page for the sayings I'm believing in</li><br/>
  <li><b>Profile:</b> Create a profile. edit profile, sign up to be a prayerperson, edit proverbs that the user has entered,            and delete profile.</li><br/>
  <li><b>User Proverbs:</b> Displays the proverbs that users have entered.</li>
</ul>
<br/>
<b>Routes</b><br/>

|HTTP Method|Endpoint|
|---|---|
|GET|/index|
|POST|/proverbs|
|GET|/proverbs/id|
|PUT|/proverbes/id|
|DELETE|/proverbes/id|
|GET|/about|
|GET|/tenets|
<br/>
<b>Stretch goals</b> <br/>
I want "proverbs For Daily Living" to change language like every second or so.</br><br/>
<b>New Features</b><br/><br/>

<b>Bruce Lee's burn your bad thoughts.</b><br/>
"I have a system of ridding my mind of negative thoughts. I visualize myself writing them down on a piece of paper. Then I imagine myself crumpling up the paper, lighting it on fire, and burning it to a crisp."
 — Bruce Lee<br/><br/>
So I'd like to have a field where you enter a negative thought, it will have to be made clear that it won't be persisted, and upon submit, get some code that either makes it look like it's burning or, crumbles up.<br/><br/></li>

I'd like to add a section with my tenets of life:<br/>

  <li>Spread Joy; Stand Firm</li>
  <li>Look around not down</li>
  <li>Do what you do</li>
  <li>Same ole G </li></li>

<br/>
  I want to make a 'prayer list' function. Basically, it's for someone to add someone to a prayer list, so that people who pray can pray for those people. I'd like to someday make this a module that churches can add to their own websites.<br/><br/>

<b>The Overview</b><br/>
I bought a book called "Proverbs for Daily Living" at a Goodwill, almost 20 years ago. All the book contains is an individual saying (called a 'proverb' by the book, but we shall call them 'Proverbs of wisdom,' or 'Proverbs' going forward.<br/><br/>

I have read this book everyday for all of these years, never skipping ahead, never going back. It has broght me tons of joy and insight.<br/><br/>

I can find nothing about this book out on the interwebs, so I have decided to bring its greatness to future generations.<br/><br/>

<b>The Project</b><br/>
I intend to build an app that displays:<br/>
<ul>
<li>The date (no year required as it all repeats every year)</li><br/>
<li>The Proverb, from the book that is associated with that day.</li><br/>
<li>A field where a user can enter their own own Proverb, complete with a submit button.</li><br/>
<li>A Twitter login feature that will either:</li><br/>
  <ul>
    <li>a) Allow the user to enter a Proverb via Twitter, and pass that Proverb back to my database<br/></li>
    <li>b) Access the user-submitted Proverbs (userProverbs)on Twitter</li><br/>
  </ul>
<li>Django login to be used for admin functions (edit and delete Proverbs).</li><br/><br/>

<b>Wireframes</b><br/><br/>
/index<br/>
![MP](https://github.com/christopherhanten/proverbsForDailyLiving/blob/master/PFDL/main_app/static/content/images/_index.png)<br/><br/>
/about<br/>
![MP](https://github.com/christopherhanten/proverbsForDailyLiving/blob/master/PFDL/main_app/static/content/images/_about.png)<br/><br/>
/signin<br/>
![MP](https://github.com/christopherhanten/proverbsForDailyLiving/blob/master/PFDL/main_app/static/content/images/_signin.png)<br/><br/>
/editprofile<br/>
![MP](https://github.com/christopherhanten/proverbsForDailyLiving/blob/master/PFDL/main_app/static/content/images/_editprofile.png)<br/><br/>
/tenets<br/>
![MP](https://github.com/christopherhanten/proverbsForDailyLiving/blob/master/PFDL/main_app/static/content/images/_tenets.png)<br/><br/>
/usernuggets<br/>
![MP](https://github.com/christopherhanten/proverbsForDailyLiving/blob/master/PFDL/main_app/static/content/images/_userNuggets.png)<br/><br/>
/prayerlist<br/>
![MP](https://github.com/christopherhanten/proverbsForDailyLiving/blob/master/PFDL/main_app/static/content/images/_prayerList.png)<br/><br/>


<b> Entity Relationship Diagram</b><br/><br/>
_under construction_<br/>

<b>User Stories</b><br/>
<b>As a USER</b><br/>
<b>I WANT TO</b> be able to load the Proverbs for Daily Living page<br/>
<b>SO THAT</b> I can see the daily Proverb<br/><br/>

<b>AS a USER</b><br/>
<b>I WANT TO</b>be able to read the Proverb<br/>
<b>SO THAT</b> I can be inspired for the day.<br/><br/>

<b>AS a USER</b><br/>
<b>I WANT TO</b> be able to see all the Proverbs, individually, from each day of the year<br/></b>
<b>SO THAT</b> each day I have something new to read.<br/><br/>

<b>AS a USER</b><br/>
<b>I WANT TO</b> be able to access the individual Proverbs from each day of the year by<br/> clicking a calendar icon<br/>
<b>SO THAT</b> I can see Proverbs form other days of the year because I do not plan on coming to this page every day.<br/><br/>

<b>AS a USER</b><br/>
<b>I WANT TO</b> have a text input field<br/>
<b>SO THAT</b> I can input userProverbs.<br/><br/>

<b>AS a USER</b><br/>
<b>I WANT TO</b> have a button to submit<br/>
<b>SO THAT</b> my Proverb will be persisted.<br/><br/>

<b>AS a USER</b><br/>
<b>I WANT TO</b> be able to add folks to a prayer list<br/>
<b>SO THAT</b> those who pray can pray for the people in need.<br/><br>

<b>AS a USER</b><br/>
<b>I WANT TO</b> enter my negative thoughts<br/>
<b>SO THAT</b> I can watch them be burnt or crumbled up.<br/><br>

<b>AS a USER</b><br/>
<b>I WANT TO</b> be able to add folks to a prayer list<br/>
<b>SO THAT</b> those who pray can pray for the people in need.<br/><br>

<b>AS a USER</b><br/>
<b>I WANT To</b> be able to go to Twitter to add a Proverb<br/>
<b>SO THAT</b> I can provide a Proverb to inspire others.<br/><br>
