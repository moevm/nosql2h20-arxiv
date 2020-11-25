import React, { useState } from "react";
import {InputGroup,FormControl} from "react-bootstrap";
import '../App.css';

export default function Category() {
    const [category, setCategory] = useState('');
    console.log(category)
    return (
        <div>
            <InputGroup size="lg" onChange={(e) => setCategory(e.target.value)}>
                <InputGroup.Prepend>
                    <InputGroup.Text id="category">By category</InputGroup.Text>
                </InputGroup.Prepend>
                <FormControl aria-label="Large" aria-describedby="inputGroup-sizing-sm" />
            </InputGroup>
        </div>
    );
}