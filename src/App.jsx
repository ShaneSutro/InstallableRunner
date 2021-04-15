import React from 'react';
import ReactDOM from 'react-dom';
import { Button } from '@vestaboard/installables'
import './style.css'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      something: "nothing",
    }
  }

  render() {
    return (
      <>
        <h1>Configured Correctly Still</h1>
        <Button buttonType="default">A Button</Button>
      </>
    )
  }
}

export default App;
