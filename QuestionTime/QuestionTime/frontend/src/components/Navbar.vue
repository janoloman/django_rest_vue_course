<template>
  <nav class="navbar navbar-expand-lg bg-light my-navbar">
    <div class="container">
      <router-link class="navbar-brand" :to="{ name: 'home' }">
        QuestionTime
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <router-link
              class="btn btn-danger"
              :to="{ name: 'question-editor' }"
            >
              Ask Question
            </router-link>
          </li>
          <li class="nav-item">
            <a class="btn btn-outline-secondary" href="/accounts/logout/"
              >Logout</a
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
};
</script>

<style>
.my-navbar {
  border-bottom: 1px solid #dddddd;
}
.navbar-brand {
  font-weight: bold;
  font-size: 150%;
}
.navbar-brand:hover {
  color: #dc3545 !important;
}
</style>