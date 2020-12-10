import React, {useState, useEffect, createRef} from "react";
import {InputGroup, FormControl, Table, Button} from "react-bootstrap";
import BootstrapTable from "react-bootstrap-table-next";
import '../App.css';
import {Link} from 'react-router-dom'
import Spinner from 'react-bootstrap/Spinner'

export default function Co_author(props) {
    const [co_author, setAuthor] = useState('');
    const [error, setError] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);
    const [result, setResult] = useState('');
    const [json, setJson] = useState([]);

    useEffect(() => {
        fetch(`http://localhost:5000/co_author?co_author=${props.match.params.co_author}`)
            .then(res => res.json())
            .then(
                (result) => {
                    setIsLoaded(true);
                    console.log(result, " - result")
                    setJson(result);
                },
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
    }, [co_author])
    const columns = [
        {
            dataField: "name",
            text: 'Coauthor name'
        },
        {
            dataField: "article",
            text: 'Article name'
        }
    ];
    if (error) {
        return <div>Ошибка: {error.message}</div>;
    } else if (!isLoaded) {
        return <Spinner animation="grow" />;
    } else {
        //console.log(author)
        return (
            <div>
                <div>
                {json.map((json_value, index) => (
                    <h2>
                        Searched author:<a href={'/author_page/' + json_value.author_id}>{json_value.author_name}</a>
                    </h2>
                ))}
                </div>
                <Table variant="dark">
                    {json.map((json_value, index) => (
                        <tr>
                            {
                                json_value.co_authors.map((value) => (
                                    <tr key={index}>
                                        <th>
                                            <a href={'/author_page/' + value.author_id}>{value.author_name}</a>
                                        </th>
                                    </tr>
                                ))
                            }
                        </tr>
                    ))}
                </Table>
                <Link to="/author">
                    <Button size="sm">
                        Back to author search
                    </Button>
                </Link>
                <Link to="/article">
                    <Button size="sm">
                        Back to article search
                    </Button>
                </Link>
            </div>
        );
    }
}
