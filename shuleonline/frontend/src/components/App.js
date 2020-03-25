import React, {Component} from 'react';
import ReactDom from 'react-dom';

class App extends Component {
    render() {
        return <h1>We made it Boooy!</h1>
    }
}

ReactDom.render(<App />, document.getElementById('app'));