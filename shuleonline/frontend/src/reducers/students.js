import { GET_STUDENT, DELETE_STUDENT } from "../actions/types";

const initialState = {
  student: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_STUDENT:
      return {
        ...state,
        student: action.payload
      };
    case DELETE_STUDENT:
      return {
        ...state,
        student: state.student.filter(student => student.id !== action.payload)
      };
    default:
      return state;
  }
}
