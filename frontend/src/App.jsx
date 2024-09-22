import {
  Button,
  Container,
  Box,
  Flex,
  Text,
  useColorMode,
  Textarea,
  Input,
  Stack,
  Spacer,
  Spinner,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import axios from "axios";

export const BASE_URL =
  import.meta.env.MODE === "development" ? "http://127.0.0.1:5000/api" : "/api";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [isLoaded, setisLoaded] = useState(false);
  const [hide, setHide] = useState("flex");
  const [showSpin, setshowSpin] = useState(false);

  const handleSubmit = async () => {
    setHide("none");
    setshowSpin(true);
    try {
      const res = await axios
        .post(BASE_URL + "/process_prompt", {
          prompt,
        })
        .then((res) => {
          console.log(res);
          setResponse(res.data.video);
        });
      setshowSpin(false);
      setisLoaded(true);
    } catch (error) {
      console.error("Error", error);
    }
  };

  return (
    <>
      <Flex bg={"gray.900"} color={"gray.100"} px={"5"} py={"5"}>
        <Box
          bg={"gray.900"}
          px={"5"}
          py={"2"}
          borderRadius={"6"}
          color={"white"}
          fontSize={"20"}
        >
          <Text fontWeight={"bold"}>RapidShorts</Text>
        </Box>
      </Flex>
      <Flex
        alignItems={"center"}
        justifyContent={"center"}
        flexDirection={"column"}
        gap={5}
        bg={"gray.900"}
        minH={"100vh"}
        color={"gray.100"}
      >
        <Flex
          flexDirection="column"
          justifyContent="center"
          minWidth="50vw"
          minH={"200"}
          bg={"gray.700"}
          px={"5"}
          py={"5"}
          borderRadius={"12"}
          display={hide}
        >
          <Box>
            <Text mb={2}>Enter your prompt</Text>
            <Input
              value={prompt}
              placeholder="Generate video of how to cut hair."
              onChange={(e) => setPrompt(e.target.value)}
            />
          </Box>
          <Spacer />
          <Box>
            <Button colorScheme="blue" size="md" onClick={handleSubmit}>
              Generate Video
            </Button>
          </Box>
        </Flex>
        <Flex minWidth={"50vw"} display={"none"}>
          <Button>Developer</Button>
          <Spacer />
          <Button>How it works</Button>
        </Flex>
        {showSpin && (
          <Flex flexDirection={"column"} gap={5} alignItems={"center"}>
            <Spinner
              thickness="4px"
              speed="0.65s"
              emptyColor="gray.200"
              color="blue.500"
              size="xl"
            />
            <Text fontSize={"medium"} color={"gray.300"}>
              Generating content, this may take a few minutes...
            </Text>
          </Flex>
        )}
        {isLoaded && (
          <Flex
            flexDirection={"column"}
            gap={5}
            alignItems={"start"}
            justifyContent={"center"}
            padding={"5"}
          >
            <video width={"1000"} controls>
              <source src={response} type="video/mp4" />
            </video>
            <Flex
              flexDirection={"column"}
              alignItems={"start"}
              gap={"3"}
              display={"none"}
            >
              <Text>Unsatisfied with the video?</Text>
              <Button size={"sm"} colorScheme="blue">
                Try different clips
              </Button>
            </Flex>
          </Flex>
        )}
      </Flex>
    </>
  );
}

export default App;
