import React from "react";
import {Route, Switch} from "react-router-dom";
import Home from "../pages/Home";
import Author from "../pages/Author";
import Category from "../pages/Category";
import Article from "../pages/Article";
import Statistics from "../pages/Statistics";

export default function Routes() {
    return (
        <Switch>
            <Route exact path="/" component={Home}/>
            <Route path="/statistics" component={Statistics}/>
            <Route path="/article" component={Article}/>
            <Route path="/category" component={Category}/>
            <Route path="/author" component={Author}/>
        </Switch>
    );
}