import React, {useState, useEffect, createRef} from "react";
import {InputGroup, FormControl, Table} from "react-bootstrap";
import '../App.css';
import Spinner from 'react-bootstrap/Spinner'

export default function Article_page(props) {
    const [article_page, setArticlePage] = useState('');
    const [error, setError] = useState(false);
    const [isLoaded, setIsLoaded] = useState(false);
    const [result, setResult] = useState('');
    const [json, setJson] = useState([]);
    let inform = createRef();
    // Примечание: пустой массив зависимостей [] означает, что
    // этот useEffect будет запущен один раз
    // аналогично componentDidMount()

    const handleChange = () => {
        //console.log('AAAAA')
        const inf = inform.current;
        if (inf !== null) {
            //console.log(inf.value)
            setArticlePage(inf.value)
        }
    }

    useEffect(() => {
        //console.log('fetch',author)
        fetch(`http://localhost:3000/api/article_page?article_page=${props.match.params.article_page}`)
            .then(res => res.json())
            .then(
                (result) => {
                    setIsLoaded(true);
                    setJson(result);
                },
                // Примечание: важно обрабатывать ошибки именно здесь, а не в блоке catch(),
                // чтобы не перехватывать исключения из ошибок в самих компонентах.
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
    }, [article_page])

    const columns = [
        {
            dataField: "author_name",
            text: 'Author name',

        },
        {
            dataField: "author_name",
            text: 'Author name',

        },
        {
            dataField: "author_name",
            text: 'Author name',

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
                <h2>
                    {json.map((value, index) => (
                        <th key={index}>{value.article_name}</th>
                    ))}
                </h2>

                <Table variant="dark">
                    <tr>
                        <td>
                            <a>Authors</a>
                        </td>
                    </tr>
                    {json.map((json_value, index) => (
                        <td >
                            {
                                json_value.authors_info.map((value) => (
                                    <tr key={index}>
                                        <th>
                                            <a href={'http://localhost:3000/author_page/' + value.author_id}>{value.author_name}</a>
                                        </th>
                                    </tr>
                                ))
                            }
                        </td>
                    ))}
                </Table>
                <div>
                    {json.map((json_value, index) => (
                        <h3>
                            doi:
                            {json_value.doi}
                        </h3>
                    ))}
                </div>
                <div>
                    {json.map((json_value, index) => (
                        <h5>
                            abstract:
                            {json_value.abstract}
                        </h5>
                    ))}
                </div>
            </div>
        );
    }
}
