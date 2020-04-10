import axios from "axios";
import { GET_STUDENT, DELETE_STUDENT } from "./types";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";
//get student object
export const getStudent = () => dispatch => {
  axios
    .get("/api/student")
    .then(res => {
      dispatch({
        type: GET_STUDENT,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};

//delete student object
export const deleteStudent = id => dispatch => {
  axios

    .delete(`/api/student/${id}/`)
    .then(res => {
      dispatch({
        type: DELETE_STUDENT,
        payload: id
      });
    })
    .catch(err => console.log(err));
};
