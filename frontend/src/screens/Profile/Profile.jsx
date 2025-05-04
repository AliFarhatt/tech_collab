import React, { useState } from "react";
import {
  Box,
  Avatar,
  Heading,
  Text,
  VStack,
  Flex,
  Grid,
  GridItem,
  Button,
  Link,
  Tag,
  Wrap,
  WrapItem,
  useDisclosure,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalBody,
  ModalCloseButton,
  ModalFooter,
  useColorModeValue,
} from "@chakra-ui/react";
import { FaLinkedin, FaPlus } from "react-icons/fa";
import { useAuth } from "../../context";
import { UserPopup } from "../../components/Popup/UserPopup/UserPopup";
import SkillsEditModal from "./components/SkillsEditModal";
import { EditIcon } from "@chakra-ui/icons";
import AddProjectModal from "./components/AddProjectModal";
import EditProjectModal from "./components/EditProjectModal";
const Profile = () => {
  const bgGradient = useColorModeValue(
    "linear(to-br, gray.50, gray.100)",
    "linear(to-br, gray.700, gray.900)"
  );
  const cardBg = useColorModeValue("white", "gray.800");
  const projectTitleColor = useColorModeValue("gray.800", "white");
  const projectBg = useColorModeValue("gray.50", "gray.900");
  const { authUser, setAuthUser } = useAuth();
  const { isOpen, onOpen, onClose } = useDisclosure();
  const {
    isOpen: isUserPopupOpen,
    onOpen: onUserPopupOpen,
    onClose: onUserPopupClose,
  } = useDisclosure();
  const {
    isOpen: isSkillsPopupOpen,
    onOpen: onSkillsPopupOpen,
    onClose: onSkillsPopupClose,
  } = useDisclosure();
  const {
    isOpen: isAddProjectPopupOpen,
    onOpen: onAddProjectPopupOpen,
    onClose: onAddProjectPopupClose,
  } = useDisclosure();
  const {
    isOpen: isEditProjectPopupOpen,
    onOpen: onEditProjectPopupOpen,
    onClose: onEditProjectPopupClose,
  } = useDisclosure();

  const [selectedProject, setSelectedProject] = useState(null);
  const [viewType, setViewType] = useState("followers"); // Modal state
  const [selectedUser, setSelectedUser] = useState(null); // To store the selected user

  // Trigger modal for followers or following
  const handleViewFollowers = () => {
    setViewType("followers");
    onOpen();
  };

  const handleViewFollowing = () => {
    setViewType("following");
    onOpen();
  };

  // Open the UserPopup modal when a user is clicked
  const handleUserClick = (user) => {
    setSelectedUser(user);
    onUserPopupOpen();
  };

  const updateFollowingList = (user) => {
    if (
      authUser.following.some((followingUser) => followingUser.id === user.id)
    ) {
      // Unfollow the user by removing them from the list
      setAuthUser((current) => {
        return {
          ...current,
          following: current.following.filter(
            (followingUser) => followingUser.id !== user.id
          ),
        };
      });
    } else {
      // Follow the user by adding them to the list
      setAuthUser((current) => {
        return {
          ...current,
          following: [...current.following, user],
        };
      });
    }
  };

  const setAuthUserSkills = (updatedSkills) => {
    setAuthUser((current) => ({
      ...current,
      skills: updatedSkills,
    }));
  };

  return (
    <Box bg={bgGradient} w="100%" minH="100vh" py={8} px={{ base: 4, md: 8 }}>
      <Grid
        templateColumns={{ base: "1fr", md: "1fr 2fr" }}
        gap={8}
        maxW="1400px"
        mx="auto"
      >
        {/* User Info */}
        <GridItem>
          <Box
            bg={cardBg}
            borderRadius="lg"
            boxShadow="lg"
            p={6}
            w="100%"
            maxW="100%"
          >
            <VStack align="center" spacing={4}>
              <Avatar
                name={authUser?.name}
                src={authUser?.profile_picture}
                size="2xl"
                boxShadow="lg"
              />
              <VStack align="center" spacing={2}>
                <Heading fontSize="2xl" fontWeight="bold" color="gray.800">
                  {authUser?.name}
                </Heading>
                <Text fontSize="lg" fontWeight="medium" color="gray.500">
                  {authUser?.general_field || "Field of Expertise"}
                </Text>
                <Text fontSize="md" color="gray.700" maxW="lg">
                  {authUser?.bio || "No bio available."}
                </Text>
                {authUser?.linkedin_profile && (
                  <Link href={authUser.linkedin_profile} isExternal>
                    <Button
                      leftIcon={<FaLinkedin />}
                      colorScheme="linkedin"
                      size="sm"
                    >
                      LinkedIn
                    </Button>
                  </Link>
                )}
                <Flex justify="space-between">
                  <Button
                    variant="ghost"
                    colorScheme="blue"
                    onClick={handleViewFollowing}
                    w="48%"
                  >
                    {authUser?.following?.length || 0} Following
                  </Button>
                  <Button
                    variant="ghost"
                    colorScheme="blue"
                    onClick={handleViewFollowers}
                    w="48%"
                  >
                    {authUser?.followers?.length || 0} Followers
                  </Button>
                </Flex>
              </VStack>
            </VStack>
          </Box>
        </GridItem>

        {/* Skills, Projects */}
        <GridItem>
          <VStack spacing={6} align="stretch">
            {/* Skills Section */}
            <Box bg={cardBg} p={6} borderRadius="lg" boxShadow="lg">
              <Flex justify="space-between" alignItems="center">
                <Heading
                  fontSize="lg"
                  fontWeight="bold"
                  color={projectTitleColor}
                >
                  Skills
                </Heading>
                <Button
                  size="sm"
                  leftIcon={<EditIcon />}
                  variant="outline"
                  colorScheme="blue"
                  onClick={onSkillsPopupOpen}
                  borderRadius="full"
                  _hover={{ bg: "blue.50" }}
                  px={4}
                >
                  Edit Skills
                </Button>
              </Flex>
              <Wrap mt={4}>
                {authUser?.skills?.length > 0 ? (
                  authUser.skills.map((skill, index) => (
                    <WrapItem key={index}>
                      <Tag size="md" colorScheme="blue">
                        {skill.skill}
                      </Tag>
                    </WrapItem>
                  ))
                ) : (
                  <Text fontSize="md" color="gray.500">
                    No skills added.
                  </Text>
                )}
              </Wrap>

              {/* Modal for editing skills */}
              <SkillsEditModal
                isOpen={isSkillsPopupOpen}
                onClose={onSkillsPopupClose}
                currentSkills={authUser?.skills || []}
                setSkills={setAuthUserSkills}
              />
            </Box>

            {/* Projects Section */}
            <Box bg={cardBg} p={6} borderRadius="lg" boxShadow="lg">
              <Flex justify="space-between" alignItems="center">
                <Heading
                  fontSize="lg"
                  fontWeight="bold"
                  color={projectTitleColor}
                  mb={4}
                >
                  Projects ({authUser?.user_projects?.length || 0})
                </Heading>
                <Button
                  colorScheme="blue"
                  onClick={onAddProjectPopupOpen}
                  leftIcon={<FaPlus />}
                  borderRadius="md" // Slightly rounded corners for a clean look
                  size="md" // Medium size, not too large
                  fontWeight="medium" // Clean, modern font weight
                  _hover={{ bg: "blue.600", color: { cardBg } }} // Simple hover effect for interactivity
                  px={6} // Padding to give it a balanced look without being too large
                >
                  Add Project
                </Button>
              </Flex>
              <VStack align="start" spacing={4} w="100%" mt={6}>
                {authUser?.user_projects?.length > 0 ? (
                  /*authUser.user_projects.map((project) => (
                    <Box
                      key={project.id}
                      w="100%"
                      bg={projectBg}
                      p={6}
                      borderRadius="lg"
                      boxShadow="lg"
                      transition="transform 0.2s"
                      _hover={{ transform: "scale(1.02)" }}
                    >
                      <VStack align="start" spacing={3}>
                        <Text
                          fontSize="xl"
                          fontWeight="600"
                          color={projectTitleColor}
                        >
                          {project.title}
                        </Text>
                        <Text fontSize="md" fontWeight="400" color="gray.500">
                          {project.description}
                        </Text>
                        {project.url && (
                          <Link href={project.url} isExternal color="blue.500">
                            Visit Project
                          </Link>
                        )}
                        <Text fontSize="sm" fontWeight="400" color="gray.500">
                          Technologies:{" "}
                          {project.technologies
                            ? project.technologies.split(", ").join(", ")
                            : "N/A"}
                        </Text>
                        <Text fontSize="sm" fontWeight="400" color="gray.500">
                          {`Status: ${project.status}, Start: ${new Date(
                            project.start_date
                          ).toLocaleDateString()}, End: ${
                            project.end_date
                              ? new Date(project.end_date).toLocaleDateString()
                              : "Ongoing"
                          }`}
                        </Text>
                      </VStack>
                    </Box>
                  ))*/
                    authUser.user_projects.map((project) => (
                      <Box
                        key={project.id}
                        w="100%"
                        bg={projectBg}
                        p={6}
                        borderRadius="lg"
                        boxShadow="lg"
                        transition="transform 0.2s"
                        _hover={{ transform: "scale(1.02)" }}
                        position="relative"
                      >
                        <Flex justify="space-between" align="center">
                          <Text
                            fontSize="xl"
                            fontWeight="600"
                            color={projectTitleColor}
                          >
                            {project.title}
                          </Text>
                          <Button
                            size="sm"
                            onClick={() => {
                              setSelectedProject(project);
                              onEditProjectPopupOpen();
                            }}
                            leftIcon={<EditIcon />}
                            variant="ghost"
                            colorScheme="blue"
                            borderRadius="md"
                          >
                            Edit
                          </Button>
                        </Flex>
    
                        <VStack align="start" spacing={3} mt={2}>
                          <Text fontSize="md" fontWeight="400" color="gray.500">
                            {project.description}
                          </Text>
                          {project.url && (
                            <Link href={project.url} isExternal color="blue.500">
                              Visit Project
                            </Link>
                          )}
                          <Text fontSize="sm" fontWeight="400" color="gray.500">
                            Technologies:{" "}
                            {project.technologies
                              ? project.technologies.split(", ").join(", ")
                              : "N/A"}
                          </Text>
                          <Text fontSize="sm" fontWeight="400" color="gray.500">
                            {`Status: ${project.status}, Start: ${new Date(
                              project.start_date
                            ).toLocaleDateString()}, End: ${
                              project.end_date
                                ? new Date(project.end_date).toLocaleDateString()
                                : "Ongoing"
                            }`}
                          </Text>
                        </VStack>
                      </Box>
                    )) 
                ) : (
                  <Text fontSize="md" color="gray.500">
                    No projects found.
                  </Text>
                )}
              </VStack>

              {/* Add Project Modal */}
              <AddProjectModal
                isOpen={isAddProjectPopupOpen}
                onClose={onAddProjectPopupClose}
                authUser={authUser}
                setAuthUser={setAuthUser}
              />
              {selectedProject && (
              <EditProjectModal
                isOpen={isEditProjectPopupOpen}
                onClose={onEditProjectPopupClose}
                project={selectedProject}
                setAuthUser={setAuthUser}
              />
            )}
            </Box>
          </VStack>
        </GridItem>
      </Grid>

      {/* Modal for Followers/Following */}
      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>
            {viewType === "followers" ? "Followers" : "Following"}
          </ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <VStack spacing={4}>
              {viewType === "followers" && authUser?.followers?.length > 0 ? (
                authUser.followers.map((user) => (
                  <Flex
                    key={user.id}
                    align="center"
                    w="100%"
                    gap={4}
                    onClick={() => handleUserClick(user)} // Open UserPopup for clicked user
                    cursor="pointer"
                    _hover={{ bg: "gray.100" }}
                    p={2}
                    borderRadius="md"
                  >
                    <Avatar
                      name={user.name}
                      src={user.profile_picture}
                      size="md"
                    />
                    <VStack align="flex-start" spacing={1}>
                      <Text fontWeight="bold">{user.name}</Text>
                      <Text fontSize="sm" color="gray.500">
                        {user.general_field}
                      </Text>
                    </VStack>
                  </Flex>
                ))
              ) : viewType === "following" &&
                authUser?.following?.length > 0 ? (
                authUser.following.map((user) => (
                  <Flex
                    key={user.id}
                    align="center"
                    w="100%"
                    gap={4}
                    onClick={() => handleUserClick(user)} // Open UserPopup for clicked user
                    cursor="pointer"
                    _hover={{ bg: "gray.100" }}
                    p={2}
                    borderRadius="md"
                  >
                    <Avatar
                      name={user.name}
                      src={user.profile_picture}
                      size="md"
                    />
                    <VStack align="flex-start" spacing={1}>
                      <Text fontWeight="bold">{user.name}</Text>
                      <Text fontSize="sm" color="gray.500">
                        {user.general_field}
                      </Text>
                    </VStack>
                  </Flex>
                ))
              ) : (
                <Text>No {viewType} found.</Text>
              )}
            </VStack>
          </ModalBody>
          <ModalFooter></ModalFooter>
        </ModalContent>
      </Modal>

      {/* User Popup */}
      {selectedUser && (
        <UserPopup
          isOpen={isUserPopupOpen}
          onClose={onUserPopupClose}
          selectedUser={selectedUser}
          setAllUsers={updateFollowingList}
          setSelectedUser={setSelectedUser}
        />
      )}
    </Box>
  );
};

export default Profile;
