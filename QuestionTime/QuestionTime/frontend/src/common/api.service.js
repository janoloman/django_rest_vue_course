// const axios = require("axios");
import axios from "axios";

// Function to retrieve a cookie by name
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

axios.default.xsrfCookieName = "xsrftoken";
axios.default.xsrfHeaderName = "X-CSRFTOKEN";

// Set CSRF token in headers
axios.defaults.headers.common['X-CSRFToken'] = getCookie('csrftoken');

export { axios };