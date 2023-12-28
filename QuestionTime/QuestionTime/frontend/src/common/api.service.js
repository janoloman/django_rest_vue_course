const axios = require("axios");

axios.default.xsrfCookieName = "xsrftoken";
axios.default.xsrfHeaderName = "X-CSRFTOKEN";

export { axios };