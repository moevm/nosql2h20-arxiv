import React from "react";
import {Route, Switch} from "react-router-dom";
import Home from "../pages/Home";
import Author from "../pages/Author";
import Co_author from "../pages/Co_authors";
import Author_page from "../pages/Author_page";
import Article_page from "../pages/Article_page";
import Category from "../pages/Category";
import Article from "../pages/Article";
import Statistics from "../pages/Statistics";

export default function Routes() {
    return (
        <Switch>
s
            <Route path="/statistics" component={Statistics}/>
            <Route path="/article" component={Article}/>
            <Route path="/category" component={Category}/>
            <Route path="/author" component={Author}/>
            <Route path="/co_author/:co_author" component={Co_author}/>
            <Route path="/author_page/:author_page" component={Author_page} />
            <Route path="/article_page/:article_page" component={Article_page} />
        </Switch>
    );
}