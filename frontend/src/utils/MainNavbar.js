import React from "react";
import {Nav, Navbar} from "react-bootstrap";
import {Link} from "react-router-dom";
import Author from "../pages/Author";
import Category from "../pages/Category";
import Article from "../pages/Article";
import Statistics from "../pages/Statistics";
import Home from "../pages/Home";

export default function MainNavbar() {
    return (
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand as={Link} to="/home">
                <i>Arxiv</i>
            </Navbar.Brand>
            <Nav defaultActiveKey="/home">
                <Nav.Item>
                    <Nav.Link as={Link} to="/home">Home</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/statistics">Statistics</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/article">Article</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/category">Category</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link as={Link} to="/author">Author</Nav.Link>
                </Nav.Item>
            </Nav>
        </Navbar>
    );

}