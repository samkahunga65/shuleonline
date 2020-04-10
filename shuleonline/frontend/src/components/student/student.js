import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getStudent, deleteStudent } from "../../actions/student";
export class Student extends Component {
  static propTypes = {
    student: PropTypes.array.isRequired
  };
  componentDidMount() {
    this.props.getStudent();
  }
  render() {
    return (
      <Fragment>
        <div className="student">
          <h3>this is the student component</h3>
          {this.props.student.map(studen => (
            <h3>
              {studen.fname}
              <button
                onClick={console.log(studen.student_id)}
                className="btn btn-sm btn-danger"
              >
                delete
              </button>
            </h3>
          ))}
          <h1></h1>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  student: state.student.student
});
export default connect(mapStateToProps, { getStudent, deleteStudent })(Student);
