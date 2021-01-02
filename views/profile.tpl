% rebase("main.tpl")

<div class="row">
    <div class="col-md-9">
        <h1>Your profile information</h1>
    </div>
    <div class="col-md-3">
        <p>You have completed <b>{{str(user.global_progress())}} %</b> of the program!</p>
        <div class="progress">
            <div class="progress-bar" role="progressbar" style="width: {{str(user.global_progress())}}%" aria-valuenow="{{str(user.global_progress())}}" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
    </div>
</div>

<div class="row">
    <div class="col-md-3">
        <p>Name<br>
        Surname<br>
        Username<br>
        Mail<br>
        Starting date</p>
    </div>
    <div class="col-md-9">
        <p>{{user.name}}<br>
        {{user.surname}}<br>
        {{user.username}}<br>
        {{user.mail}}<br>
        {{user.starting_date}}</p>
    </div>
</div>