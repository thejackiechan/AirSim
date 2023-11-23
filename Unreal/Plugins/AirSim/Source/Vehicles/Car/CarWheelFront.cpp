// Copyright 1998-2017 Epic Games, Inc. All Rights Reserved.

#include "CarWheelFront.h"
#include "UObject/ConstructorHelpers.h"

UCarWheelFront::UCarWheelFront()
{
    // ShapeRadius = 18.f;
    // ShapeWidth = 15.0f;
    // Mass = 20.0f;
    // DampingRate = 0.25f;
    WheelRadius = 38.f;
    WheelWidth = 17.0f;
    bAffectedByHandbrake = false;
    // SteerAngle = 40.f;
    bAffectedBySteering = true;
    MaxSteerAngle = 50.f;
    AxleType = EAxleType::Front;

    // Setup suspension forces
    SuspensionForceOffset = FVector(0.0f, 0.0f, 0.0f);
    SuspensionMaxRaise = 10.0f;
    SuspensionMaxDrop = 10.0f;
    // SuspensionNaturalFrequency = 9.0f;
    // SuspensionDampingRatio = 1.05f;
    SuspensionDampingRatio = 1.5f;

    // Find the tire object and set the data for it
    // static ConstructorHelpers::FObjectFinder<UTireConfig> TireData(TEXT("/AirSim/VehicleAdv/Vehicle/WheelData/Vehicle_FrontTireConfig.Vehicle_FrontTireConfig"));
    // TireConfig = TireData.Object;
}
