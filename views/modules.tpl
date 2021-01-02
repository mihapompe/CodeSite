% rebase("main.tpl")

<div class="row">
    <div class="col-md-9">
        <h1>Modules</h1>
    </div>
    <div class="col-md-3">
        <p>You have completed <b>{{str(user.global_progress())}} %</b> of the program!</p>
        <div class="progress">
            <div class="progress-bar" role="progressbar" style="width: {{str(user.global_progress())}}%" aria-valuenow="{{str(user.global_progress())}}" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
    </div>
</div>


% for module in modules_list:
    % if module.module_number in user.enabled_modules:
        <div class="row">
            <div class="col-md-9">
                <div class="card">
                    <!--<img src="..." class="card-img-top" alt="...">-->
                    <div class="card-body">
                        <h5 class="card-title">Module {{module.module_number}} - {{module.title}}</h5>
                        <p class="card-text">{{module.description}}</p>
                        <a href="/modules/module{{module.module_number}}" class="btn btn-primary">Start exercises</a>
                    </div>
                </div>
            </div>
        </div>
        <br>
    % end
% end