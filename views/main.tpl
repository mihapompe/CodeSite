<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="../static/bootstrap.min.css" rel="stylesheet">
    <link href="/static/pricing.css" rel="stylesheet">
    <link href="/static/navbar.css" rel="stylesheet">
    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <title>CodeSite</title>
  </head>

  <body>
    <!-- Navigation bar -->
    <nav class="navbar navbar-expand navbar-dark bg-dark" aria-label="Second navbar example">
      <div class="container-fluid">
        <a class="navbar-brand" href="/modules">CodeSite</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample02" aria-controls="navbarsExample02" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarsExample02">
          <ul class="navbar-nav me-auto">
            <li class="nav-item active">
              <a class="nav-link" href="/instructions">Instructions</a>
            </li>
            % if user.admin == True:
            <li class="nav-item active">
              <a class="nav-link" aria-current="page" href="/dashboard">Dashboard</a>
            </li>
            % end
          </ul>
          <ul class="navbar-nav me-right">
            <li class="nav-item dropdown active">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">Hello, {{user.name}}</a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="/profile">Profile</a></li>
                <li><a class="dropdown-item" href="/stats">Stats</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="/logout">Log out</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <main class="container">
      {{!base}}
    </main>

    <!-- Footer -->
    <footer class="footer pt-4 my-md-5 pt-md-5 border-top">
      <div class = "container">
      <div class="row">
        <div class="col-12 col-md">
          <img class="mb-2" src="../static/python_logo.png" alt="" width="22" height="22">
          <small class="d-block mb-3 text-muted">&copy; 2021, Miha Pompe</small>
        </div>
        <div class="col-6 col-md">
          <!--<h5>Features</h5>
          <ul class="list-unstyled text-small">
            <li><a class="link-secondary" href="#">Cool stuff</a></li>
            <li><a class="link-secondary" href="#">Random feature</a></li>
            <li><a class="link-secondary" href="#">Team feature</a></li>
            <li><a class="link-secondary" href="#">Stuff for developers</a></li>
            <li><a class="link-secondary" href="#">Another one</a></li>
            <li><a class="link-secondary" href="#">Last time</a></li>
          </ul>-->
        </div>
        <div class="col-6 col-md">
          <h5>Resources</h5>
          <ul class="list-unstyled text-small">
            <li><a class="link-secondary" href="/debugging">How to debug your code</a></li>
            <li><a class="link-secondary" href="https://www.w3schools.com/python/default.asp" target="_blank">W3Schools</a></li>
            <li><a class="link-secondary" href="https://docs.python.org/3/" target="_blank">Python documentation</a></li>
          </ul>
        </div>
        <div class="col-6 col-md">
          <h5>About</h5>
          <ul class="list-unstyled text-small">
            <li><a class="link-secondary" href="/about">About</a></li>
            <li><a class="link-secondary" href="mailto: pompe.miha@gmail.com">Contact me</a></li>
            <li><a class="link-secondary" href="https://github.com/mikepompi/CodeSite" target="_blank">GitHub</a></li>
            <li><a class="link-secondary" href="/license">License</a></li>
          </ul>
        </div>
      </div>
      </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
  </body>
</html>