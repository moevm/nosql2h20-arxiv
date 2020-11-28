import React, {useState, useEffect, createRef} from "react";
import {InputGroup, FormControl, Table, Button} from "react-bootstrap";
import BootstrapTable from "react-bootstrap-table-next";
import '../App.css';
import {Link} from 'react-router-dom'
import Spinner from 'react-bootstrap/Spinner'

export default function Author_page(props) {
    const [author_page, setAuthor] = useState('');
    const [error, setError] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);
    const [result, setResult] = useState('');
    const [json, setJson] = useState([]);

    useEffect(() => {
        console.log(props)
        fetch(`http://localhost:5000/author_page?author_page=${props.match.params.author_page}`)
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
    }, [author_page])

    const columns = [
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
        //console.log(json)
        return (
            <div>
                <div>
                    <Table variant="dark">
                        <th>
                            {json.map((json_value, index) => (
                                <h2>
                                    {json_value.author_name}
                                </h2>
                            ))}
                        </th>
                        <th>
                            {json.map((json_value, index) => (
                                <Button variant="success" size='lg'
                                        href={'http://localhost:3000/co_author/' + json_value.author_id}>
                                    Go to coauthors
                                </Button>
                            ))}
                        </th>
                    </Table>
                </div>
                <Table variant="dark">
                    <thead>
                        <tr>
                            {columns.map((value, index) => (
                                <th key={index}>{value.text}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {json.map((json_value, index) => (
                            <tr>
                                {
                                    json_value.articles.map((value) => (
                                        <tr key={index}>
                                            <th>
                                                <a href={'http://localhost:3000/article_page/' + value.article_id}>{value.article_name}</a>
                                            </th>
                                        </tr>
                                    ))
                                }
                            </tr>
                        ))}
                    </tbody>
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
