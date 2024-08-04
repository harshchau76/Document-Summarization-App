import React, { useState } from 'react';
import FileUpload from './FileUpload';
import Summarize from './Summarize';

function App() {
    const [filePath, setFilePath] = useState('');

    return (
        <div>
            <FileUpload onFileUpload={setFilePath} />
            {filePath && <Summarize filePath={filePath} />}
        </div>
    );
}

export default App;
