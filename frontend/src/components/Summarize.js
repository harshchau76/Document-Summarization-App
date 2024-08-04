import React, { useState } from 'react';

function Summarize({ filePath }) {
    const [summary, setSummary] = useState('');

    const handleSummarize = async () => {
        const response = await fetch('http://localhost:8000/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: filePath }),
        });

        const result = await response.json();
        setSummary(result.summary);
    };

    return (
        <div>
            <button onClick={handleSummarize}>Summarize</button>
            <div>
                <h3>Summary:</h3>
                <p>{summary}</p>
            </div>
        </div>
    );
}

export default Summarize;
