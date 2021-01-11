% rebase("main.tpl")

<div class="row">
    <div class="col-md-9">
        <h1>Modules</h1>
    </div>
    <div class="col-md-3">
        <p>You have completed <b>{{str(user.global_progress())}} %</b> of the program!</p>
        <div class="progress">
            % if user.global_progress() == 100:
            <div class="progress-bar bg-success" role="progressbar" style="width: {{str(user.global_progress())}}%" aria-valuenow="{{str(user.global_progress())}}" aria-valuemin="0" aria-valuemax="100"></div>
            % else:
            <div class="progress-bar" role="progressbar" style="width: {{str(user.global_progress())}}%" aria-valuenow="{{str(user.global_progress())}}" aria-valuemin="0" aria-valuemax="100"></div>
            % end
        </div>
    </div>
</div>


% for module in modules_list:
    <div class="row">
        <div class="col-md-9">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Module {{module.module_number}} - {{module.title}}</h5>
                    <p class="card-text">{{module.description}}</p>
                    % score = str(round(sum(user.progress[module.module_number-1])/len(user.progress[module.module_number-1]),1))
                    <div class="row">
                        <div class="progress col-md-6" style="height: 5px;">
                            % if score == "100.0":
                            <div class="progress-bar bg-success" role="progressbar" style="width: {{score}}%" aria-valuenow="{{score}}" aria-valuemin="0" aria-valuemax="100"></div>
                            % else:
                            <div class="progress-bar" role="progressbar" style="width: {{score}}%" aria-valuenow="{{score}}" aria-valuemin="0" aria-valuemax="100"></div>
                            % end
                        </div>
                        <div class="col-md-3"></div>
                        <div class="col-md-3">
                        % if module.module_number in user.enabled_modules:
                            <a href="/modules/module{{module.module_number}}" class="btn btn-primary">Start exercises</a>
                        % else:
                            <a href="/modules/module{{module.module_number}}" class="btn btn-primary disabled" disabled>Start exercises</a>
                        % end
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <br>
% end