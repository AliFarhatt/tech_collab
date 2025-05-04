import React, { useEffect, useState } from "react";
import {
  VStack,
  Input,
  Button,
  Text,
  Box,
  useColorModeValue,
  Flex,
} from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import { AUTH_ROUTE } from "../../../../constants/routes";
import { toast } from "react-toastify";
import { signUp } from "../../../../services/AuthApi";
import { LogoHeader } from "../../../../components";
import PasswordInput from "../../../../components/UI/PasswordInput/PasswordInput";

const RegisterForm = ({ setDidSubmit }) => {
  const cardBg = useColorModeValue("white", "gray.800");
  const inputBg = useColorModeValue("gray.50", "gray.700");
  const buttonBg = useColorModeValue("blue.500", "blue.600");
  const navigate = useNavigate();
  const [isFormValid, setIsFormValid] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [registeredInfo, setRegisteredInfo] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setRegisteredInfo((prevInfo) => ({
      ...prevInfo,
      [name]: value,
    }));
  };

  const validateForm = () => {
    const { name, email, password, confirmPassword } = registeredInfo;

    if (!name || !email || !password || !confirmPassword) {
      setIsFormValid(false);
      return;
    }

    if (password.length < 8 || password !== confirmPassword) {
      setIsFormValid(false);
      return;
    }

    setIsFormValid(true);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    const body = {
      name: registeredInfo.name,
      email: registeredInfo.email,
      password: registeredInfo.password,
    };

    try {
      const response = await signUp(body);
      if (response.status) {
        console.log(response);
        toast.success(response.message);
        setDidSubmit(true);
      } else {
        toast.error(
          response?.message || "Registration failed. Please try again."
        );
      }
    } catch (error) {
      toast.error(error?.message || "Registration failed. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  const login = () => {
    navigate(`/${AUTH_ROUTE}`);
  };

  useEffect(() => {
    validateForm();
  }, [registeredInfo]);

  return (
    <Flex justify="center" align="center" h="100vh" width="100%">
      <Box
        maxW="400px"
        width="100%"
        p={6}
        bg={cardBg}
        borderRadius="lg"
        boxShadow="xl"
        border="1px solid"
        borderColor={useColorModeValue("gray.200", "gray.700")}
      >
        <LogoHeader />
        <Text
          fontSize="3xl"
          color={useColorModeValue("gray.800", "white")}
          textAlign="center"
          mb={6}
          fontWeight={600}
        >
          Register
        </Text>

        <form onSubmit={handleSubmit}>
          <VStack spacing={4} align="start" w="100%">
            {/* Full Name Input */}
            <Input
              placeholder="Full Name"
              value={registeredInfo.name}
              onChange={handleInputChange}
              bg={inputBg}
              focusBorderColor="blue.400"
              required
              size="md"
              borderRadius="md"
              fullWidth
              name="name"
            />

            {/* Email Input */}
            <Input
              type="email"
              placeholder="Enter Email"
              value={registeredInfo.email}
              onChange={handleInputChange}
              bg={inputBg}
              focusBorderColor="blue.400"
              required
              size="md"
              borderRadius="md"
              fullWidth
              name="email"
            />

            {/* Password Input */}
            <PasswordInput
              placeholder="Enter Password"
              value={registeredInfo.password}
              onChange={handleInputChange}
              bg={inputBg}
              focusBorderColor="blue.400"
              required
              size="md"
              borderRadius="md"
              fullWidth
              name="password"
            />

            {/* Confirm Password Input */}
            <PasswordInput
              placeholder="Confirm Password"
              value={registeredInfo.confirmPassword}
              onChange={handleInputChange}
              bg={inputBg}
              focusBorderColor="blue.400"
              required
              size="md"
              borderRadius="md"
              fullWidth
              name="confirmPassword"
            />

            {/* Register Button */}
            <Button
              type="submit"
              colorScheme="blue"
              bg={buttonBg}
              width="100%"
              borderRadius="md"
              mt={4}
              isDisabled={!isFormValid}
              isLoading={isLoading}
            >
              Register
            </Button>
          </VStack>
        </form>

        <Text
          fontSize="sm"
          textAlign="center"
          mt={4}
          color={useColorModeValue("gray.600", "gray.300")}
        >
          Already have an account?{" "}
          <Text as="span" color="blue.400" cursor="pointer" onClick={login}>
            Login
          </Text>
        </Text>
      </Box>
    </Flex>
  );
};

export default RegisterForm;
