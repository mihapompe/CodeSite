% rebase("main.tpl")

<div class="py-5 text">
  <h2>Add user</h2>
  <p class="lead">All fields must be filled. Make sure you use correct data types. Grant admin privileges only to 
  chosen users.</p>
</div>

<div class="row g-3">

  </div>
  <div class="col-md-7 col-lg-8">
    <h4 class="mb-3">User attributes</h4>
    <form action="/add_user" method="post" enctype="multipart/form-data">
      <div class="row g-3">
        <div class="col-sm-6">
          <label for="name" class="form-label">Name</label>
          <input name="name" type="text" class="form-control" id="name" placeholder="Name" value="" required>
        </div>

        <div class="col-sm-6">
          <label for="surname" class="form-label">Surname</label>
          <input type="text" class="form-control" id="surname" name="surname" placeholder="Surname" value="" required>
        </div>

        <div class="col-sm-6">
          <label for="username" class="form-label">Username</label>
          <input name="username" type="text" class="form-control" id="username" placeholder="Username" value="" required>
        </div>

        <div class="col-sm-6">
          <label for="password" class="form-label">Password</label>
          <input type="text" class="form-control" id="password" name="password" placeholder="Password" value="" required>
        </div>

        <div class="col-12">
          <label for="mail" class="form-label">Mail</label>
          <div class="input-group">
            <input type="text" class="form-control" id="mail" name="mail" placeholder="Mail" required>
          </div>
        </div>

        <div class="col-sm-4">
          <label for="starting_date_year" class="form-label">Starting date - year</label>
          <input type="text" class="form-control" id="starting_date_year" name="starting_date_year" placeholder="Year" value="" required>
        </div>

        <div class="col-sm-4">
          <label for="starting_date_month" class="form-label">Starting date - month</label>
          <input type="text" class="form-control" id="starting_date_month" name="starting_date_month" placeholder="Month" value="" required>
        </div>

        <div class="col-sm-4">
          <label for="starting_date_day" class="form-label">Starting date - day</label>
          <input type="text" class="form-control" id="starting_date_day" name="starting_date_day" placeholder="Day" value="" required>
        </div>

        <div class="my-3">
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="save-info" name="admin">
            <label class="form-check-label" for="save-info">Admin</label>
          </div>
        </div>

      </div>
      <br>
      <button class="w-100 btn btn-primary btn-lg" type="submit">Add user</button>
    </form>
  </div>
</div>