# DotNet Intern Project

## Introduction

For the last two weeks as a intern at Prosper IT Consultining, I had worked with  my peers in developing and debugging a full scale MVC application. Working on a legacy codebase was a great learning oppertunity for fixing bugs, cleaning up code, and adding requested features. There were some big changes that could have been a large time sink, but we used what we had to deliver what was needed on time. I saw how a good developer works with what they have to make a quality product.  Because much of the site had already been built, there were also a good deal of front end stories and UX improvements that needed to be completed, all of varying degrees of difficulty. Everyone on the team had a chance to work on front end and back end stories. Over the two week sprint I also had the opportunity to work on some other project management and team programming skills that I'm confident I will use again and again on future projects.

## Front-end Bug

Among the work that I had, I had to rearrange and delete some buttons. Using Bootstrap Docs I had assigned different classes in order to provide desirable results.

```html
<div class="iconBtnContainer">
    <button class="iconBtn" onclick="window.location.href ='@Url.Action("Create", "Sponsors")'">
        <!-- or buttons can be in their own container-->
        <i class="fa fa-plus-square fa-fw"></i>Create New<!-- This button is a link to a different page -->
    </button>
</div>

<div class="iconBtnContainer">
    <button class="iconBtn" onclick="window.location.href ='@Url.Action("Index", "Sponsors")'">
        <!-- This button is a link to a different page-->
        <i class="fa fa-hand-point-left fa-fw"></i>Back To List<!-- This button is a link to a different page -->
    </button>
</div>

```