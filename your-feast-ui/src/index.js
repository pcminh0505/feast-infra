import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

import FeastUI from "@feast-dev/feast-ui";
import "@feast-dev/feast-ui/dist/feast-ui.css";
// import CustomComponent from "./custom-component";

const BASE_URL = process.env.REACT_APP_HOST_URL || "localhost:8000";

ReactDOM.render(
  <React.StrictMode>
    <FeastUI
      feastUIConfigs={{
        projectListPromise: fetch(`${BASE_URL}/projects`, {
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => {
            return response.json();
          })
          .catch((error) => {
            console.log(error);
          }),
      }}
    />
  </React.StrictMode>,
  document.getElementById("root")
);
