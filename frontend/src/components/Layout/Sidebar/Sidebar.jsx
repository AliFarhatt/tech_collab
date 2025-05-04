import React from "react";
import {
  Box,
  Button,
  Flex,
  Icon,
  Image,
  Text,
  useColorModeValue,
  VStack,
} from "@chakra-ui/react";
import {
  faBookmark,
  faCodeBranch,
  faHistory,
  faLightbulb,
  faSignOut,
  faStar,
  faUser,
  faUsers,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { logoEmblem as darkLogoEmblem, whiteLogoEmblem } from "../../../assets";
import {
  EXPLORE_PROJECTS_ROUTE,
  EXPLORE_USERS_ROUTE,
  GENERATE_PROJECTS_ROUTE,
  PROFILE_ROUTE,
  RECOMMENDED_PROJECTS_ROUTE,
  SAVED_PROJECTS_ROUTE,
  SESSIONS_HISTORY_ROUTE,
} from "../../../constants/routes";
import { useLocation, useNavigate } from "react-router-dom";
import { useModal } from "../../../hooks";
import { logout } from "../../../services/AuthApi";
import { toast } from "react-toastify";
import { useAuth } from "../../../context";
import { TOKEN_KEY } from "../../../context/AuthContext";
import LogoutPopup from "./components/LogoutPopup";

const Sidebar = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { checkAuthentication } = useAuth();
  const { openModal, closeModal, isModalOpened } = useModal();

  const sidebarButtons = [
    { name: "Explore Users", logo: faUsers, route: EXPLORE_USERS_ROUTE },
    {
      name: "Explore Projects",
      logo: faLightbulb,
      route: EXPLORE_PROJECTS_ROUTE,
    },
    
    {
      name: "Generate Projects",
      logo: faCodeBranch,
      route: GENERATE_PROJECTS_ROUTE,
    },
    {
      name: "Sessions History",
      logo: faHistory,
      route: SESSIONS_HISTORY_ROUTE,
    },
    { name: "Saved Projects", logo: faBookmark, route: SAVED_PROJECTS_ROUTE },
  ];

  const handleLogout = async () => {
    try {
      const response = await logout();
      if (response.status) {
        localStorage.setItem(TOKEN_KEY, "");
        await checkAuthentication();
      } else {
        toast.error(response.message);
      }
    } catch (error) {
      toast.error(error.message);
    }
  };

  const primaryColor = useColorModeValue("blue.500", "blue.200");
  const sidebarBg = useColorModeValue("#F8F8F8", "gray.800");
  const iconColor = useColorModeValue("black", "white");
  const activeButtonColor = useColorModeValue("white", "gray.700");
  const logoEmblem = useColorModeValue(darkLogoEmblem, whiteLogoEmblem);

  return (
    <Box
      w="250px"
      h="100vh"
      bg={sidebarBg}
      boxShadow="lg"
      display="flex"
      flexDirection="column"
      justifyContent="space-between"
    >
      {/* Logout Popup */}
      <LogoutPopup
        isOpen={isModalOpened}
        onClose={closeModal}
        primaryButtonText="Logout"
        handleSubmit={handleLogout}
      />

      {/* Sidebar Header */}
      <Flex direction="column" align="center" py={6}>
        <Image src={logoEmblem} alt="Logo" boxSize="50px" mb={2} />
        <Text fontSize="xl" fontWeight="bold">
          Tech-Collab
        </Text>
      </Flex>

      {/* Sidebar Buttons */}
      <VStack spacing={4} align="stretch" px={4}>
        {sidebarButtons.map((button) => (
          <Button
            key={button.name}
            leftIcon={<Icon as={FontAwesomeIcon} icon={button.logo} />}
            bg={
              location.pathname.includes(button.route)
                ? primaryColor
                : "transparent"
            }
            color={
              location.pathname.includes(button.route)
                ? activeButtonColor
                : iconColor
            }
            justifyContent="flex-start"
            variant="solid"
            _hover={{ bg: primaryColor, color: activeButtonColor }}
            onClick={() => navigate(`/${button.route}`)}
          >
            {button.name}
          </Button>
        ))}
      </VStack>

      {/* Sidebar Footer */}
      <VStack spacing={4} align="stretch" px={4} mb={6}>
        <Button
          leftIcon={<Icon as={FontAwesomeIcon} icon={faUser} />}
          bg={
            location.pathname.includes(PROFILE_ROUTE)
              ? primaryColor
              : "transparent"
          }
          color={
            location.pathname.includes(PROFILE_ROUTE)
              ? activeButtonColor
              : iconColor
          }
          justifyContent="flex-start"
          _hover={{ bg: primaryColor, color: activeButtonColor }}
          onClick={() => navigate(`/${PROFILE_ROUTE}`)}
        >
          Your Profile
        </Button>
        <Button
          leftIcon={<Icon as={FontAwesomeIcon} icon={faSignOut} />}
          justifyContent="flex-start"
          variant="solid"
          bg="transparent"
          color={iconColor}
          _hover={{ bg: primaryColor, color: activeButtonColor }}
          onClick={openModal}
        >
          Logout
        </Button>
      </VStack>
    </Box>
  );
};

export default Sidebar;
