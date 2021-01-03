% rebase("main.tpl")

<h2>Dashboard</h2>
<div class="table-responsive">
  <table class="table table-striped table-sm">
    <thead>
      <tr>
        <th>Name</th>
        <th>Surname</th>
        <th>Username</th>
        <th>Mail</th>
        <th>Starting date</th>
        <th>Admin</th>
        <th>Global progress</th>
        <th>Enabled modules</th>
        <th>More info</th>
      </tr>
    </thead>
    <tbody>
      % for user_ in users:
      <tr>
        <td>{{user_.name}}</td>
        <td>{{user_.surname}}</td>
        <td>{{user_.username}}</td>
        <td><a href="mailto: {{user_.mail}}">{{user_.mail}}</a></td>
        <td>{{user_.starting_date}}</td>
        <td>{{user_.admin}}</td>
        <td>{{user_.global_progress()}} %</td>
        <td>{{user_.enabled_modules}}</td>
        <td><a href="/stats/{{user_.username}}" class="btn btn-primary btn-sm">Info</a></td>
      </tr>
      % end
    </tbody>
  </table>
  <a href="/add_user" class="btn btn-primary">Add user</a>
</div>

