import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      something: "nothing",
    }
  }

  render() {
    return (
      <h1>Configured Correctly Still</h1>
    )
  }
}

export default App;
