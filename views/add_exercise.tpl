% rebase("main.tpl")

<div class="py-5 text">
  <h2>Add exercise</h2>
  <p class="lead">Module and exercise numbers are filled out automatically, but can still be changed. Select the correct type of exercise and select the file/s you with to import.</p>
</div>

<div class="row g-3">
  <div class="col-md-5 col-lg-4 order-md-last">
    <h4 class="d-flex justify-content-between align-items-center mb-3">
      <span class="text-muted">Cheatsheet</span>
    </h4>
    <ul class="list-group mb-3">
      <li class="list-group-item d-flex justify-content-between lh-sm">
        Code
        <code>&ltcode&gt&lt/code&gt</code>
      </li>
      <li class="list-group-item d-flex justify-content-between lh-sm">
        Code group
        <code>&ltpre&gt&ltcode&gt&lt/code&gt&lt/pre&gt</code>
      </li>
      <li class="list-group-item d-flex justify-content-between lh-sm">
        Variable <code>&ltvar&gt&lt/var&gt</code>
      </li>
      <li class="list-group-item d-flex justify-content-between lh-sm">
        Sample output <code>&ltsamp&gt&lt/samp&gt</code>
      </li>
    </ul>

  </div>
  <div class="col-md-7 col-lg-8">
    <h4 class="mb-3">Exercise attributes</h4>
    <form action="/add_exercise/{{module_number}}" method="post" enctype="multipart/form-data">
      <div class="row g-3">
        <div class="col-sm-6">
          <label for="module_number" class="form-label">Module number</label>
          <input name="module_number" type="text" class="form-control" id="module_number" placeholder="" value="{{module_number}}" required>
        </div>

        <div class="col-sm-6">
          <label for="exercise_number" class="form-label">Exercise number</label>
          <input type="text" class="form-control" id="exercise_number" name="exercise_number" placeholder="" value="{{exercise_number}}" required>
        </div>

        <div class="col-12">
          <label for="username" class="form-label">Title</label>
          <div class="input-group">
            <input type="text" class="form-control" id="title" name="title" placeholder="Title" required>
          </div>
        </div>

        <div class="col-12">  
          <label for="username" class="form-label">Description</label>
          <div class="input-group">
            <textarea type="text" class="form-control" id="description" name="description" placeholder="Description" value="" rows="15"></textarea>
          </div>
        </div>

        <div class="col-12">
          <label for="state" class="form-label">Type</label>
          <select class="form-select" id="type" name="type" required>
            <option value="exercise">Exercise</option>
            <option value="text">Text</option>
            <option value="video">Video</option>
          </select>
        </div>
        
        <div class="col-12">
            <label class="form-label" for="customFile">Add test file/s</label>
            <input name="test_files" type="file" class="form-control" id="customFile" multiple/>
        </div>

      </div>
      <br>
      <button class="w-100 btn btn-primary btn-lg" type="submit">Add exercise</button>
    </form>
  </div>
</div>