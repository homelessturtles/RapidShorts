import {
  Input,
  Button,
  Container,
  Box,
  Flex,
  Text,
  useColorMode,
} from "@chakra-ui/react";


function App() {
  return (
    <>
      <Container>
        <Text>RapidShorts</Text>
        <Box>
          <Text>Enter your prompt</Text>
          <Input placeholder="Generate video of how to cut hair." />
          <Button colorScheme="blue" size="sm">
            Generate Video
          </Button>
        </Box>
      </Container>
    </>
  );
}
export default App;
