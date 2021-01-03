% rebase("main.tpl")

<div class="row">
    <div class="col-md-9">
        <h1>Module {{module.module_number}} - {{module.title}}</h1>
    </div>
    <div class="col-md-3">
        % score = str(round(sum(user.progress[module.module_number-1])/len(user.progress[module.module_number-1]),1))
        <p>You have completed <b>{{score}} %</b> of this module!</p>
        <div class="progress">
            <div class="progress-bar" role="progressbar" style="width: {{score}}%" aria-valuenow="{{score}}" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
    </div>
</div>

% if user.admin == True:
    <div class="row">
        <div class="col-md-6">
            <a href="/add_exercise/{{module.module_number}}" class="btn btn-primary">Add exercise</a>
        </div>
    </div>
    <br>
% end

% for j, exercise in enumerate(module.exercises):
    % print(module.exercises)
    <div class="row">
        <div class="col-md-9">
            <div class="card">
                <div class="card-body">
                    <h4 class="card-title">{{exercise.type.capitalize()}} {{exercise.exercise_number}} - {{exercise.title}}</h4>
                    <p>{{exercise.description}}</p>
                    % if exercise.type == "exercise":
                        % score = str(user.progress[module.module_number-1][j])
                        % if user.admin == True:
                            <div class="row">
                                <div class="progress col-md-6" style="height: 5px;">
                                    <div class="progress-bar" role="progressbar" style="width: {{score}}%;" aria-valuenow="{{score}}" aria-valuemin="0" aria-valuemax="100"></div>
                                </div><br>
                                <div class="col-md-3"></div>
                                <div class="col-md-3">
                                    <a href="/{{module.module_number}}/{{exercise.exercise_number}}" class="btn btn-primary">Add part</a>
                                </div>
                            </div>
                            <br>
                        % else:
                            <div class="progress col-md-6" style="height: 5px;">
                                <div class="progress-bar" role="progressbar" style="width: {{score}}%;" aria-valuenow="{{score}}" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                            <br>
                        % end
                        % for i, subexercise in enumerate(exercise.subexercises):
                            <h5>Part {{i+1}}</h5>
                            <p class="card-text">{{!subexercise}}</p>
                        % end
                        % if len(exercise.download_files) == 0:
                            <a href="/download_exercises/{{module.module_number}}/{{exercise.exercise_number}}" class="btn btn-primary disabled">Download exercises</a>
                            <a href="/download_tester/{{module.module_number}}/{{exercise.exercise_number}}" class="btn btn-primary disabled">Download tester</a>
                        % else:
                            <a href="/download_exercises/{{module.module_number}}/{{exercise.exercise_number}}" class="btn btn-primary">Download exercises</a>
                            <a href="/download_tester/{{module.module_number}}/{{exercise.exercise_number}}" class="btn btn-primary">Download tester</a>
                        % end
                    % elif exercise.type == "text":
                        % for i, subexercise in enumerate(exercise.subexercises):
                            <h5>Part {{i+1}}</h5>
                            <p class="card-text">{{!subexercise}}</p>
                        % end
                        <a href="/mark_as_completed/{{module.module_number}}/{{exercise.exercise_number}}" class="btn btn-primary">Mark as completed</a>
                    % elif exercise.type == "video":
                        <video class="col-md-12" poster="/static/python_logo.png" controls>
                            <source src="/static/{{exercise.video_file}}" type="video/mp4">
                                Your browser does not support this video.
                        </video>
                        % for i, subexercise in enumerate(exercise.subexercises):
                            <h5>Part {{i+1}}</h5>
                            <p class="card-text">{{!subexercise}}</p>
                        % end
                        % if len(exercise.download_files) != 0:
                        <br>
                        <a href="/download_exercises/{{module.module_number}}/{{exercise.exercise_number}}" class="btn btn-primary">Download file</a>
                        % end
                        <a href="/mark_as_completed/{{module.module_number}}/{{exercise.exercise_number}}" class="btn btn-primary">Mark as completed</a>
                    % end
                </div>
            </div>
        </div>
    </div>
    <br>
% end

