import React from 'react';
import ReactDOM from 'react-dom';
import { Button, Title, SubTitle, Small, Toast } from '@vestaboard/installables'
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
        <Title>Installable</Title>
        <SubTitle>A Runner</SubTitle>
        <Button buttonType="default">A Button</Button>
        <Toast message="Success!" severity="success" open="true"></Toast>
        <Small>Powered by Shane Sutro</Small>
      </>
    )
  }
}

export default App;
