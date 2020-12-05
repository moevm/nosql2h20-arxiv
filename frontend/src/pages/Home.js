import React, {useState} from "react";
import {Dropdown,Form, FormControl, Table, Spinner, Button} from "react-bootstrap";
import '../App.css';
import axios from 'axios';


export default function Home() {
    const [zipfile, setZipfile] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [Loadedmsg,setLoadedmsg] = useState("");
    const onFileChange = event => {
        setZipfile(event.target.files[0]);
	setLoadedmsg("Loaded");

    };
    console.log(zipfile)
    const onFileUpload = () => {
        const formData = new FormData();
        formData.append(
            zipfile.name,
            zipfile
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
            <FormControl
                type="file"
                onChange={onFileChange}/>
            <h2>Import</h2>
            <Button variant={"success"} onClick={onFileUpload}>
                Import
            </Button>
            <div>
            {isLoading ?  <Spinner animation="grow" /> : <h2>{Loadedmsg}</h2>}
            </div>
            <h2>Export</h2>
            <a href={"http://localhost:80/api/home"} target="_blank" rel="noopener noreferrer" download>
                <Button>
                    <i className="fas fa-download"/>
                    Download File
                </Button>
            </a>

        </div>
    )
        ;
}
