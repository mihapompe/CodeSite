% rebase("main.tpl")

<div class="row">
    <div class="col-md-9">
        <h1>Your progress</h1>
    </div>
    <div class="col-md-3">
        <p>You have completed <b>{{str(user.global_progress())}} %</b> of the program!</p>
        <div class="progress">
            <div class="progress-bar" role="progressbar" style="width: {{str(user.global_progress())}}%" aria-valuenow="{{str(user.global_progress())}}" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
    </div>
</div>
<br>
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
            % for mod_num, exer in enumerate(user.progress):
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