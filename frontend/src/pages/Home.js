import React, {useState} from "react";
import {Dropdown,Form, FormControl, Table, Spinner, Button} from "react-bootstrap";
import '../App.css';
import axios from 'axios';

const AUTHOR = "author"
const ARTICLE = "article"
const WROTE = "wrote"


export default function Home() {
    const [zipfile, setZipfile] = useState("");
    const [typeNode, setTypenode] = useState(ARTICLE)
    const [isLoading, setIsLoading] = useState(false);

    const onFileChange = event => {
        setZipfile(event.target.files[0]);

    };
    console.log(zipfile)
    const onFileUpload = () => {
        const formData = new FormData();
        formData.append(
            typeNode,
            zipfile,
            zipfile.name
        );
        console.log(formData)
        setIsLoading(true);

        axios.post("api/home", formData).then(res => {
            console.log(res.data);
            console.log(res.data["error"]);
            console.log("error" in res.data);
            if ("error" in res.data) {
                alert(res.data["error"])
                setIsLoading(false);
            } else {
                console.log(res.status);
                setIsLoading(false);
            }

        });
    };


    return (
        <div>
            <Dropdown>
                <Dropdown.Toggle variant="primary" id="dropdown-basic">
                    {typeNode}
                </Dropdown.Toggle>

                <Dropdown.Menu>
                    <Dropdown.Item onClick={() => setTypenode(AUTHOR)}>{AUTHOR}</Dropdown.Item>
                    <Dropdown.Item onClick={() => setTypenode(ARTICLE)}>{ARTICLE}</Dropdown.Item>
                    <Dropdown.Item onClick={() => setTypenode(WROTE)}>{WROTE}</Dropdown.Item>
                </Dropdown.Menu>
            </Dropdown>
            <FormControl
                type="file"
                onChange={onFileChange}/>
            <h2>Import</h2>
            <Button variant={"success"} onClick={onFileUpload}>
                Import
            </Button>


            <h2>Export</h2>
            <a href={"/home"} target="_blank" rel="noopener noreferrer" download>
                <Button>
                    <i className="fas fa-download"/>
                    Download File
                </Button>
            </a>

        </div>
    )
        ;
}