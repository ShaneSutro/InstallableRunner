import React from 'react';
import ReactDOM from 'react-dom';
import { Button, Title, SubTitle, Small, Toast, Icon } from '@vestaboard/installables'
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
        <Icon type="check" color="white"/>
        <Button buttonType="default" endIcon={<Icon type="check" />}>Save Changes</Button>
        <Small>Powered by Shane Sutro</Small>
      </>
    )
  }
}

export default App;
