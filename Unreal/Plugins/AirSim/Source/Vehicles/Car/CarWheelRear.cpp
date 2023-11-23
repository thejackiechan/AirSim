// Copyright 1998-2017 Epic Games, Inc. All Rights Reserved.

#include "CarWheelRear.h"
#include "UObject/ConstructorHelpers.h"

UCarWheelRear::UCarWheelRear()
{
    // ShapeRadius = 18.f;
    // ShapeWidth = 15.0f;
    WheelRadius = 38.f;
    WheelWidth = 17.0f;
    bAffectedByHandbrake = true;
    // SteerAngle = 0.f;
    MaxSteerAngle = 0.f;
    AxleType = EAxleType::Rear;

    // Setup suspension forces
    SuspensionForceOffset = FVector(0.0f, 0.0f, 0.0f);
    SuspensionMaxRaise = 10.0f;
    SuspensionMaxDrop = 10.0f;
    // SuspensionNaturalFrequency = 9.0f;
    // SuspensionDampingRatio = 1.05f;
    SuspensionDampingRatio = 1.5f;

    // Find the tire object and set the data for it
    // static ConstructorHelpers::FObjectFinder<UTireConfig> TireData(TEXT("/AirSim/VehicleAdv/Vehicle/WheelData/Vehicle_BackTireConfig.Vehicle_BackTireConfig"));
    // TireConfig = TireData.Object;
}
