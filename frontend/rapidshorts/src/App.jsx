import {
  Button,
  Container,
  Box,
  Flex,
  Text,
  useColorMode,
  Textarea,
  Input,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:5000/api/process_prompt", {
        prompt,
      });
      setResponse(res.data.video);
    } catch (error) {
      console.error("Error", error);
    }
  };

  return (
    <>
      <Container>
        <Text>RapidShorts</Text>
        <Box>
          <Text>Enter your prompt</Text>
          <Input
            value={prompt}
            placeholder="Generate video of how to cut hair."
            onChange={(e) => setPrompt(e.target.value)}
          />
          <Button colorScheme="blue" size="sm" onClick={handleSubmit}>
            Generate Video
          </Button>
          <video controls>
            <source src={response} type="video/mp4" />
          </video>
          <a href={response}>{response}</a>
        </Box>
      </Container>
    </>
  );
}

export default App;
