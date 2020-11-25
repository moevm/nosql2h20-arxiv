import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter} from 'react-router-dom';
import Routes from "./utils/Routes";
import MainNavbar from "./utils/MainNavbar";


function App() {

  return (
      <BrowserRouter>
        <MainNavbar/>
        <Routes/>
      </BrowserRouter>
  );
}

export default App;
