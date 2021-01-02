% rebase("main.tpl")

<div class="row">
    <div class="col-md-9">
        <h1>About CodeSite</h1>
    </div>
</div>

<div class="row">
    <div class="col-md-9">
        Website for learning and testing Python.

        <h4>User mode</h4>
        To enter the site a user must enter it's credentials (<code>username</code> 
        and <code>password</code>). He can optionally opt out of saving their login. 
        The main page is the modules page, where the user can see all the modules 
        available to them. A new module is made available to them every week. 
        Progress of the entire program or module can be seen on the right side. 
        Inside every module the user can see different exercises, their descriptions 
        and some examples. The download files button will download all the necessary 
        Python files (<code>name_exercise.py</code> and <code>name_tester.py</code>). 
        Exercises are solved in the _exercise.py file and to test them against 
        test cases you run <code>_tester.py</code>. The tester file will evaluate the user's code 
        and send the final score back to this website.

        <h4>Admin mode</h4>
        Admin is a normal user and has the same features, but also a few additional ones. In this mode you can:
        <ul>
            <li>See all user data (except passwords) and their progress</li>
            <li>Add new users</li>
            <li>Add new exercises and test files</li>
        </ul>

        <h4>Requirements</h4>
        Before you begin, ensure you have met the following requirements:
        <ul>
            <li>You have Python 3 and packages Bottle and Json installed.</li>
            <li>To run tested files you should also install Numpy.</li>
        </ul>

        <h4>How to install and run this project</h4>
        <ul>
            <li>Clone the repository to your desired location.</li>
            <li>Run the file <code>controller.py</code> using by running <code>python controller.py</code></li>
        </ul>

        <h4>Resources</h4>
        <ul>
            <li><a href=https://bottlepy.org/docs/dev/index.html>Bottle documentation</a></li>
            <li><a href=https://getbootstrap.com/docs/5.0/getting-started/introduction>Bootstrap examples and documentation</a></li>
        </ul>
    </div>
</div>
