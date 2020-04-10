import React, { Component, Fragment } from "react";
import ReactDom from "react-dom";

import { Provider } from "react-redux";
import store from "../store";
// import "./App.css";
import Student from "./student/student";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Fragment>
          <h1>ooo yes</h1>
          <Student />
        </Fragment>
      </Provider>
    );
  }
}

ReactDom.render(<App />, document.getElementById("app"));
