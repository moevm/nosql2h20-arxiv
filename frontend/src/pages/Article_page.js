import React, { useState} from "react";
import {InputGroup,FormControl} from "react-bootstrap";
import '../App.css';

export default function Article_page() {
    const [article, setArticle] = useState('');
    console.log(article)
    return (
        <div>
            <InputGroup size="lg" onChange={(e) => setArticle(e.target.value)}>
                <InputGroup.Prepend>
                    <InputGroup.Text id="article" >By article</InputGroup.Text>
                </InputGroup.Prepend>
                <FormControl aria-label="Large" aria-describedby="inputGroup-sizing-sm" />
            </InputGroup>
        </div>
    );
}