% rebase("main.tpl")

<div class="row">
    <div class="col-md-9">
        <h1>{{user_.name}} {{user_.surname}}</h1>
    </div>
    <div class="col-md-3">
        <p>He/she has completed <b>{{str(user_.global_progress())}} %</b> of the program!</p>
        <div class="progress">
            <div class="progress-bar" role="progressbar" style="width: {{str(user_.global_progress())}}%" aria-valuenow="{{str(user_.global_progress())}}" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
    </div>
</div>
<br>

<div class="row">
    <div class="col-md-3">
        <p>Name<br>
        Surname<br>
        Username<br>
        Mail<br>
        Starting date<br>
        Enabled modules<br>
        Admin
        </p>
    </div>
    <div class="col-md-9">
        <p>{{user_.name}}<br>
        {{user_.surname}}<br>
        {{user_.username}}<br>
        <a href="mailto: {{user_.mail}}">{{user_.mail}}</a><br>
        {{user_.starting_date}}<br>
        {{user_.enabled_modules}}<br>
        {{user_.admin}}</p>
    </div>
</div>

<div class="row">
    <div class="table-responsive">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th>Module number</th>
              <th>Exercise number</th>
              <th>Score</th>

            </tr>
          </thead>
          <tbody>
            % for mod_num, exer in enumerate(user_.progress):
                % for exer_num, exer_score in enumerate(exer):
                    <tr>
                        <td>{{mod_num+1}}</td>
                        <td>{{exer_num+1}}</td>
                        % if exer_score == 100:
                        <td class="text-success">{{exer_score}} %</td>
                        % else:
                        <td>{{exer_score}} %</td>
                        % end
                    </tr>
                % end
            % end
          </tbody>
        </table>
    </div>
</div>